from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index), 
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('users/<int:restaurant_id>', views.restaurant_events)
]