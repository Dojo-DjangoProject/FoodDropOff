from django.db import models
import re
from datetime import datetime
import bcrypt

# Create your models here.

class Location(models.Model):
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip_code = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Restaurant(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=70)
    restaurant_name = models.CharField(max_length=255)
    cuisine = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    location = models.ForeignKey(Location, related_name="location_restaurants", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Event(models.Model):
    restaurant_id =  models.ForeignKey(Restaurant, related_name="restaurant_events", on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    notes = models.TextField()
    location = models.ForeignKey(Location, related_name="location_events", on_delete=models.CASCADE)
    minimum_orders = models.IntegerField()
    maximum_orders = models.IntegerField()
    minimum_amount_per_order = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Item(models.Model):
    event_id =  models.ForeignKey(Event, related_name="event_items", on_delete=models.CASCADE)
    item_title = models.CharField(max_length=255)
    item_description = models.TextField()
    item_price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
