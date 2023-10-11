from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Item, Cart, CartItem, Hold

# Create your views here.

def item_list(request):
    items = Item.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'holder/item_list.html', {'items':items})

def cart_list(request):
    cart_items = CartItem.objects.filter()

def add_to_cart(request, item_id):
    item = Item.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity', 1))

    if item.is_available(quantity):
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart.add_item(item, quantity)
        return redirect('item_list')
    else:
        return render(request, 'holder/out_of_stock.html')