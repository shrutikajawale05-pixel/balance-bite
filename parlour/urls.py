from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu_page, name='menu'),
    path('cart/', views.cart, name='cart'),
    path('payment/', views.payment, name='payment'),
    path('order-success/', views.order_success, name='order_success'), 
    path("payment/", views.payment, name="payment"),
]