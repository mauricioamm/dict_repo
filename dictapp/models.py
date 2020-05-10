from django.db import models

from django.conf import settings

class dictclass(models.Model):
    palavra = models.CharField(max_length=255, null=False, blank=False)
    palavratrad = models.CharField(max_length=1000, null=False, blank=False)
    frase = models.CharField(max_length=1000, null=False, blank=False)
    frasetrad = models.CharField(max_length=1000, null=False, blank=False)
    figura1 = models.CharField(max_length=1000, null=False, blank=False)
    som1 = models.CharField(max_length=1000, null=False, blank=False)

    def __str__(self):
        return self.palavra + ' ' + self.frase

    objetos = models.Manager()

