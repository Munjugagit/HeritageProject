from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Sub_counties
from .models import Historicalsite

# Create your views here.
class HomePageView(TemplateView):
    template_name = "index.html"

def subcounty_datasets(request):
    subcounty = serialize('geojson', Sub_counties.objects.all())
    return HttpResponse(subcounty,content_type='json')

def historicalsite_points(request):
    historicalsite = serialize('geojson', Historicalsite.objects.all())
    return HttpResponse(historicalsite,content_type='json')