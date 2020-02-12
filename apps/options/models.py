from django.contrib.auth.models import Group
from django.db import models

# Create your models here.


class SiteConfiguration(models.Model):
    PADRAO = 'padrao'
    STYLE_CHOICES = [
        (PADRAO, 'Padrão'),
        ('cosmo', 'Cosmo'),
        ('flatly', 'Flatly'),
        ('litera', 'Litera'),
        ('lumen', 'Lumen'),
        ('materia', 'Materia'),
        ('sketchy', 'Sketchy'),
    ]

    name = models.CharField(max_length=10, primary_key=True)
    style = models.CharField(max_length=15, choices=STYLE_CHOICES, default=PADRAO)
    group = models.OneToOneField(
        Group, blank=False, related_query_name='site_configurations', unique=True, on_delete=models.PROTECT
    )
    created_date = models.DateTimeField(auto_now_add=True)
