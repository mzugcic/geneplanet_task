import gzip
import re
from itertools import islice

from django.core.management import BaseCommand

from genomes.models import Genome


class Command(BaseCommand):
    help = 'Parse gziped VCF file to create Genome objects'

    def add_arguments(self, parser):
        parser.add_argument(
            'file',
            type=str,
            help='Add absolute path to your gziped vcf file intended for parsing'
        )
        parser.add_argument(
            "--bulk-limit",
            type=int,
            default=2000,
            required=False,
            help='''
                Set how many lines should be parsed at a time, before bulk
                creating objects. Take into consideration that the higher the
                number the longer it could take to process the file. By default
                the limit is set to 2000.
            '''
        )
        parser.add_argument(
            "--parse-count",
            type=int,
            default=None,
            required=False,
            help='''
                Set how many lines should be parsed and objects created from the
                file. This is useful if you don't need all objects & just need
                to test stuff. Defaults to `None` meaning the whole file is
                being parsed.
            '''
        )

    def handle(self, *args, **options):
        bulk_limit = options['bulk_limit']
        parse_count = options['parse_count']

        if bulk_limit > 10000:
            raise ValueError('''
                You should not set the bulk limit over 10,000. See "--help" for more
                information.
            ''')

        with gzip.open(options['file'], 'rt') as file:
            data_list = (
                re.split(r'\t+', line.rstrip('\n')) for line in file
                if not line.startswith('#')
            )

            genome_objs = self._get_objects(data_list, parse_count)

            while True:
                batch = list(islice(genome_objs, bulk_limit))
                if not batch:
                    break

                Genome.objects.bulk_create(batch, bulk_limit)

    def _get_objects(self, data_list, parse_count):
        """
        Return a Genome objects generator.

        If parse_count exists, return only the asked number of objects.
        """
        if parse_count:
            return (self._set_object(data) for i, data in zip(range(parse_count), data_list))

        return (self._set_object(data) for data in data_list)

    def _set_object(self, data):
        """Return a Genome object & strip char field of whitespaces."""
        return Genome(
            chrom=data[0],
            pos=data[1],
            rsid=data[2].strip(),
            ref=data[3].strip(),
            alt=data[4].strip(),
            info=data[5].strip(),
        )