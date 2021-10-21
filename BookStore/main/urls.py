from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # Main Pages
    path('', views.index, name='home'),
    path('products', views.products, name='products'),
    path('product-details', views.productDetalis, name='product-details'),
    path('about', views.about, name='about'),
    path('account', views.account, name='account'),
    path('cart', views.cart, name='cart'),



    # Lab-8
    path('index-8', views.index8, name='index-8'),
    path('team-8', views.team8, name='team-8'),
    path('contacts-8', views.contacts8, name='contacts-8'),

]
