# HOME APP URLS

from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Ourstory
from django.contrib import messages

# Create your views here.

def menus(request):    
    return render(request, "index.html")
    
def breakfast(request):    
    return render(request, "breakfast.html")

def drinks(request):
    return render(request, "drinks.html")

def reservations(request):
    return render(request, "reservations.html")

def delivery(request):
    return render(request, "delivery.html")

def ourstory(request):

    if request.method == "POST":    
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")

        obj = Ourstory(name = name, email=email, phone=phone, address=address, date=datetime.today())        
        obj.save()
        messages.success(request, 'Your Response has been submitted..!!!')
    return render(request, "ourstory.html")
