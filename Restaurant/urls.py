from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index), #render homepage
    path('login', views.login),
    path('register', views.register),
]