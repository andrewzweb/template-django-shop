from django.shortcuts import render, redirect
from .models import Product
from cart.forms import CartAddProductForm
from django.urls import reverse_lazy
from .forms import CreateProductForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product/list.html', {'products': products})

def product_item(request, product_slug):
    product = Product.objects.get(slug=str(product_slug))
    cart_product_form = CartAddProductForm()
    return render(request, 'product/item.html', {'product': product, 'cart_product_form':cart_product_form})

def product_add(request):
    form = CreateProductForm()
    if request.method == 'POST':
        form = CreateProductForm(request.POST)
        if form.is_valid():
            form.save()
            product = Product.objects.last()
            return redirect(reverse_lazy('catalog:item', kwargs={'product_slug':product.slug}))
        return render(request, 'product/add.html', {'form': form})
    return render(request, 'product/add.html', {'form': form})
