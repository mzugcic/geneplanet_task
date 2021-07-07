import re

from django.http import JsonResponse
from django.shortcuts import render

from genomes.models import Genome


def index(request):
    """Index view to serve the template."""
    return render(request, 'genomes/index.html', {})


def genomes(request):
    """
    API view to return searched Genome objects

    Returns already structured HTML for dispaly.
    """
    search = request.GET.get('search')
    if re.search(r"\s", search):
        search_params = search.split()
        qs = Genome.objects.filter(
            chrom=search_params[0],
            pos=search_params[1],
        )
    else:
        qs = Genome.objects.filter(
            rsid__icontains=search
        )

    return JsonResponse({"html": render_html(qs)})


def render_html(data):
    """Return structured HTML for given Genome data."""

    html_genomes = ["""
        <tr>
            <th>{}</th>
            <th>{}</th>
            <th>{}</th>
            <th>{}</th>
            <th>{}</th>
            <th>{}</th>
        </tr>
    """.format(
        genome.rsid,
        genome.chrom,
        genome.pos,
        genome.ref,
        genome.alt,
        genome.info
    ) for genome in data]

    return """
        <table>
            <tr style="background: gray">
                <th style="min-width: 50px">RSID</th>
                <th style="min-width: 50px">CHROM</th>
                <th style="min-width: 50px">POS</th>
                <th style="min-width: 50px">REF</th>
                <th style="min-width: 50px">ALT</th>
                <th style="min-width: 50px">INFO</th>
            </tr>
            {}
        </table>
    """.format('\n'.join(html_genomes))
