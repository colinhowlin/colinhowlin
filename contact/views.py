from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def contact_index(request):
    return HttpResponse("Contact page")
