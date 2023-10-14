from django.urls import path 
from . import views 


urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('cart/', views.cart_list, name='cart_list'),
    path('add_to_cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('checkout/<int:cart_id>', views.place_holds, name='place_holds'),
]