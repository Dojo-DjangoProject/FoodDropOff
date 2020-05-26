from django.db import models
# import re
# from datetime import datetime
# import bcrypt
from Restaurant.models import *

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=70)
    phone_number = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Order(models.Model):
    user_id =  models.ForeignKey(User, related_name="user_orders", on_delete=models.CASCADE)
    item_id = models.ManyToManyField(Item, related_name="item_orders")
    event_id = models.ForeignKey(Event, related_name="event_orders", on_delete=models.CASCADE)
    status = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Message(models.Model):
    order_id =  models.ForeignKey(Order, related_name="order_messages", on_delete=models.CASCADE)
    sent_by = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class OrderQuantity(models.Model):
    item_id =  models.ForeignKey(Item, related_name="item_quantities", on_delete=models.CASCADE)
    order_id =  models.ForeignKey(Order, related_name="order_quantities", on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
