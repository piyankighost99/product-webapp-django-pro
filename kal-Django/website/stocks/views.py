from django.shortcuts import render,HttpResponse
from .models import companyInformation
from stocks import home, items, contact_us, sign
# Create your views here.

def home(request):
     info=companyInformation.objects.all().first()
     return render(request, 'home.html')

def display_items(request):
    info = companyInformation.objects.all().first()
    products = items.objects.all()
    
    data = {
        'info': info,
        'products': products
    }
    
    return render(request, 'items.html', data)

def contact_us(request):
    
    return render(request,'contact_us.html')

def sign(request):
    return render(request,'sign.html')
