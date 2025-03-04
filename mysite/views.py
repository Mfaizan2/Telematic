from django.http import HttpResponse
from django.shortcuts import render

def home (request):
    data =  {
        "title": "Home",
        "clist": ['Python', "django", "laravel"],
        "numbers":[],
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

def user_form(request):
    ans = 0
    try:
        n1 = int(request.GET['num1'])
        n2 = int(request.GET['num2'])
        ans = n1+n2
    except:
        pass
    return render(request, "forms.html",{"output" : ans})
