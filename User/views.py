from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'registration.html')

def logout(request):
    pass

def restaurant_events(request,restaurant_id):
    
    # upcoming_events = Event.objects.all().order_by(date_time > today)
    
    context = {
        # 'upcoming_events' : upcoming_events
    }
    return render(request,'restaurantevents.html',context)