from django.db import models

# Create your models here.

class Item(models.Model):
    '''Represents an item within the library and is assigned appropriate attributes'''

    name = models.CharField(max_length=100, null=False)
    stock = models.PositiveIntegerField(default=1, null=False)
    item_type = models.CharField(max_length=25, null=False)
    author = models.CharField(max_length=50)
    description = models.TextField()

    def is_available(self, quantity=1):
        '''Will return a boolean indicating whether there is enough stock'''

        return self.stock >= quantity

    def __str__(self):
        '''Will return a string representation of the Item object'''

        return self.name



class Cart(models.Model):
    '''Represents a Cart data object that stores CartItem object's in an items attribute'''

    items = models.ManyToManyField(Item, through='CartItem')

    def add_item(self, item, quantity=1):
        '''Will create a new CartItem object or update an existing one and add it to the Cart data object'''

        if item.is_available(quantity):
            cart_item, created = CartItem.objects.get_or_create(cart=self, item=item)
            if not created:
                cart_item.quantity += quantity
                cart_item.save()
            else:
                cart_item.quantity = quantity
                cart_item.save()
        else:
            raise Exception('This item is completely checked out.')
        
    def remove_item(self, item, quantity=1):
        '''Will remove a CartItem object from the existing Cart object instance'''

        try:
            cart_item = CartItem.objects.get(cart=self, item=item)
        except CartItem.DoesNotExist:
            return
        if cart_item.quantity <= quantity:
            cart_item.delete()
        else:
            cart_item.quantity -= quantity
            cart_item.save()

    def clear_cart(self):
        '''Will clear the Cart object of all CartItem objects'''

        cart_items = CartItem.objects.filter(cart=self)
        for item in cart_items:
            item.delete()



class CartItem(models.Model):
    '''Represents an Item object that has been added to a Cart object'''

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)



class Hold(models.Model):
    '''Represents a Hold object that is created upon checking out with a Cart object'''

    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def place_holds(self, cart):
        '''Will create Hold objects for each CartItem object in a Cart'''
        


    def __str__(self):
        '''Returns a string representation of the hold'''

        return f"Hold for {self.item}"