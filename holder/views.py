from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Item, Cart, CartItem, Hold
from .utils import generate_unique_identifier

# Create your views here.

def item_list(request):
    items = Item.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'holder/item_list.html', {'items':items})

def cart_list(request):
    cart_items = CartItem.objects.filter()
    return render(request, 'holder/cart.html')

def add_to_cart(request, item_id):
    item = Item.objects.get(pk=item_id)
    quantity = int(request.POST['quantity'])

    if item.is_available(quantity):
        cart_id = request.session.get('cart_id')

        if not cart_id:
            cart_id = generate_unique_identifier()
            request.session['cart_id'] = cart_id
        
        cart, created = Cart.objects.get_or_create(cart_id=cart_id)
        cart.add_item(item, quantity)
        return redirect('cart_list')
    else:
        return render(request, 'holder/out_of_stock.html')