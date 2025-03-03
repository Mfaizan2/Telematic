from django.http import HttpResponse
from django.shortcuts import render

def home (request):
    return render(request, "index.html")

def aboutUs (request):
    return HttpResponse("welcome to mysite")

def portfolio (request, portid):
    return HttpResponse(portid)
