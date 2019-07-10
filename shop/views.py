from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def shop_index(request):
    return HttpResponse("Shop page")
