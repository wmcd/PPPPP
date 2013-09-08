from django.http import HttpResponse
from django.core import serializers

from PPPPP.models import Sponsor, Api, Prize

def index(request):
  return HttpResponse('Herp derp')

def sponsors(request):
  data = serializers.serialize('json', Sponsor.objects.all()) 
  return HttpResponse(data)

def apis(request):
  data = serializers.serialize('json', Api.objects.all())
  return HttpResponse(data)

def prizes(request):
  data = serializers.serialize('json', Prize.objects.all())
  return HttpResponse(data)
