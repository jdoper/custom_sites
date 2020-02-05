from django import forms

from apps.options.models import *


class SiteConfiguration(forms.ModelForm):
    class Meta:
        model = SiteConfiguration
        fields = ['name', 'style', 'group']
