from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blog_index(request):
    return HttpResponse("Blog page")
