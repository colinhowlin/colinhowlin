from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_index(request):
    return HttpResponse("Home page")
