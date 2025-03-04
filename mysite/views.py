from django.http import HttpResponse
from django.shortcuts import render, redirect

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
    if request.method == 'GET':
        output = request.GET['output']
    return render(request, 'about.html', {'output':output})


def portfolio (request, portid):
    return HttpResponse(portid)

def submitForm(request):
    return HttpResponse(request)


def user_form(request):
    ans = 0
    data = {}
    try:
        if request.method == 'POST':
            n1 = int(request.POST['num1'])
            n2 = int(request.POST['num2'])
            ans = n1+n2
            data = {
                "n1": n1,
                'n2':n2,
                'output':ans
            }
            url = '/aboutus/?output={}'.format(ans)
            return redirect(url)
    except:
        pass
    return render(request, "forms.html",data)


