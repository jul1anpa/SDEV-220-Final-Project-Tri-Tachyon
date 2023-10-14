from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Inheriting from models.Model tells Django that the class
# is a representation of a database table (think of an entity).

# Each attribute would be treated as a field (or column) in the 
# database. 

# This step allows yours classes to interact with a database
# through Django's Object-Relational-Mapping system, or ORM.

class Item(models.Model):
    name = models.CharField(max_length=255, unique=True)
    availability = models.PositiveIntegerField(default=1)
    item_type = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Cart(models.Model):
    items = models.ManyToManyField(Item, through='CartItem')

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class Hold(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Hold for {self.item}"

