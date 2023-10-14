from django.db import models
from django.utils import timezone


# Create your models here.

class Item(models.Model):
    '''Represents an item within the library and is assigned appropriate attributes'''

    name = models.CharField(max_length=100, null=False)
    stock = models.PositiveIntegerField(default=1, null=False)
    item_type = models.CharField(max_length=25, null=False)
    author = models.CharField(max_length=50)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='images/', null=True)

    def is_available(self, quantity=1):
        '''Will return a boolean indicating whether there is enough stock'''

        return self.stock >= quantity

    def __str__(self):
        '''Will return a string representation of the Item object'''

        return self.name



class Cart(models.Model):
    '''Represents a Cart data object that stores CartItem object's in an items attribute'''

    session_key = models.CharField(max_length=32, null=True)
    items = models.ManyToManyField(Item, through='CartItem')
        


class CartItem(models.Model):
    '''Represents an Item object that has been added to a Cart object'''

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)



class Hold(models.Model):
    '''Represents a Hold object that is created upon checking out with a Cart object'''

    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        '''Returns a string representation of the hold'''

        return f"Hold for {self.item}"