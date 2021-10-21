from django.shortcuts import render

# Main Site

def index(request):
    return render(request, 'main/index.html')

def products(request):
    return render(request, 'main/products.html')

def productDetalis(request):
    return render(request, 'main/product-details.html')

def about(request):
    return render(request, 'main/about.html')

def account(request):
    return render(request, 'main/account.html')

def cart(request):
    return render(request, 'main/cart.html')



# Lab 8

def index8(request):
    return render(request, 'main/index-8.html')

def team8(request):
    return render(request, 'main/team-8.html')

def contacts8(request):
    return render(request, 'main/contacts-8.html')
