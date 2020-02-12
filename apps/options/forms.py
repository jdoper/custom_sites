from django import forms

from apps.options.models import *


class SiteConfiguration(forms.ModelForm):
    class Meta:
        model = SiteConfiguration
        fields = ['name', 'style', 'group']
        labels = {
            'name': 'Nome',
            'style': 'Estilo',
            'group': 'Grupo',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'style': forms.Select(attrs={'class': 'form-control'}),
            'group': forms.Select(attrs={'class': 'form-control'}),
        }
