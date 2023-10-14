from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Item, Cart, CartItem, Hold
from django.shortcuts import get_object_or_404
from django.db import transaction



def item_list(request):
    items = Item.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'holder/item_list.html', {'items':items})



def cart_list(request):
    if 'cart_id' in request.session and Cart.objects.filter(id=request.session['cart_id']):
        try:
            cart = get_object_or_404(Cart, id=request.session['cart_id'])
            cart_items = CartItem.objects.filter(cart=cart)
            total_quantity = sum(cart_item.quantity for cart_item in cart_items)
            return render(request, 'holder/cart.html', {'cart_items': cart_items, 'cart': cart, 'total_quantity': total_quantity})
        except Cart.DoesNotExist:
            return render(request, 'holder/cart.html')
    else:
        return render(request, 'holder/cart.html')



def add_to_cart(request, item_id):
    item = Item.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))

    if 'cart_id' not in request.session or Cart.objects.filter(id=request.session['cart_id']).exists() == False:
        session_key = request.session.session_key
        cart = Cart.objects.create(session_key=session_key)
        request.session['cart_id'] = cart.id
    else:
        cart = Cart.objects.get(id=request.session['cart_id'])

    if item.is_available(quantity):
        cart_item, created = CartItem.objects.get_or_create(cart=cart, item=item)
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
        else:
            cart_item.quantity = quantity
            cart_item.save()
        return redirect('cart_list')  
    else:
        return redirect('item_list')



def place_holds(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    cart_items = CartItem.objects.filter(cart=cart)
    total = 0
    with transaction.atomic():
        for cart_item in cart_items:
            item = cart_item.item
            quantity = cart_item.quantity
            total += quantity
            hold = Hold(item=item, quantity=quantity)
            hold.save()
            item.stock -= quantity
            item.save()
        cart.delete()
    return render(request, 'holder/checkout.html', {'total': total})