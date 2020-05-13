from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product/list.html', {'products': products})

def product_item(request, product_slug):
    product = Product.objects.get(slug=str(product_slug))
    return render(request, 'product/item.html', {'product': product})

