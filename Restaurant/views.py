from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    # Render homepage
    pass

def login(request):
    return render(request,'restaurant-login.html')

def register(request):
    return render(request,'restaurant-registration.html')