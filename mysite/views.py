from django.http import HttpResponse
from django.shortcuts import render

def home (request):
    data =  {
        "title": "Home",
        "clist": ['Python', "django", "laravel"],
        "students":[
            {"name":"Ali", "id": 24},
            {"name":"Arman", "id": 25},
        ]
    }
    return render(request, "index.html", data)

def aboutUs (request):
    return HttpResponse("welcome to mysite")

def portfolio (request, portid):
    return HttpResponse(portid)
