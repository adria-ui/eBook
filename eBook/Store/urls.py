from django.urls import path
from . import views

urlpatterns = [
    path('', views.store_view),
    path('cart_add_item/', views.cart_add_item),
    path('cart/', views.cart_view),
    path('cart/del_cart_item/', views.del_cart_item)
]