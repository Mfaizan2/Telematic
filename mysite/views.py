from django.http import HttpResponse
from django.shortcuts import render, redirect
from service.models import Service

def home (request):
    serviceData = Service.objects.all().order_by('service_title')
    data =  {
        'servicedata': serviceData
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


