from django.shortcuts import render
from django.http import HttpResponse

from apps.options.forms import SiteConfiguration


def index(request):
    if request.method == 'POST':
        form = SiteConfiguration(request.POST)
    else:
        form = SiteConfiguration()

    return render(request, 'options/index.html', {'form': form})
