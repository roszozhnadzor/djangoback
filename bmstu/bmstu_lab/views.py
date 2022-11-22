from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from bmstu_lab.models import Cakes
from bmstu_lab.models import Tastes

def hello(request):
    return render(request, 'index.html', { 'data' : {
        'current_date': date.today(),
        'list': ['python', 'django', 'html']
    }})
def GetOrders(request):
    return render(request, 'orders.html', {'data' : {
        'cakes':  Cakes.objects.all()
    }})
def GetCatalog(request):
    return render(request, 'catalog.html')

def GetOrder(request, id):
    return render(request, 'order.html', {'data' : {
        'cake': Cakes.objects.filter(id=id)[0],
        'tastes': Tastes.objects.filter(nameid=id)[0]
    }})