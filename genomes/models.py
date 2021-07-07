from django.db import models


class Genome(models.Model):
    chrom = models.IntegerField()
    pos = models.IntegerField()
    rsid = models.CharField(max_length=1024)
    ref = models.CharField(max_length=1024)
    alt = models.CharField(max_length=1024)
    info = models.CharField(max_length=1024)

    class Meta:
        indexes = [
            models.Index(fields=['rsid', ]),
            models.Index(fields=['chrom', 'pos', ]),
        ]
