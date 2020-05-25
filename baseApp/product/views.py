from django.shortcuts import render
from .models import Product
from cart.forms import CartAddProductForm, CartAddProductHideQuantityForm

def product_list(request):
    products = Product.objects.all()
    cart_product_form = CartAddProductHideQuantityForm()
    return render(request, 'product/list.html', {'products': products, 'cart_product_form':cart_product_form})

def product_item(request, product_slug):
    product = Product.objects.get(slug=str(product_slug))
    cart_product_form = CartAddProductForm()
    return render(request, 'product/item.html', {'product': product, 'cart_product_form':cart_product_form})


