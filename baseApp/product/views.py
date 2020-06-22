from django.shortcuts import render, redirect
from django.urls import reverse
from product.models import Product, Category
from cart.forms import CartAddProductForm, CartAddProductHideQuantityForm
from product.forms import ProductForm


def product_list(request, category_slug=None):
    if category_slug:
        target_category = Category.objects.get(category_slug=category_slug)
        categories = Category.objects.all()
        products = Product.objects.filter(category=target_category)
    else:
        categories = Category.objects.all()
        products = Product.objects.all()
    cart_product_form = CartAddProductHideQuantityForm()
    return render(request, 'product/list.html', locals())


def product_item(request, product_slug):
    categories = Category.objects.all()
    product = Product.objects.get(slug=str(product_slug))
    cart_product_form = CartAddProductForm()
    return render(request, 'product/item.html', locals())


def product_add(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect(reverse('catalog:list'))
    return render(request, 'product/add.html', {'form': form})


def product_edit(request, product_slug):
    product = Product.objects.get(slug=str(product_slug))

    form = ProductForm(instance=product)
    if request.method == "POST":
        new_form = ProductForm(request.POST, request.FILES, instance=product)
        if new_form.is_valid():
            new_form.save()
            return redirect(reverse('catalog:item',
                                    kwargs={'product_slug': product.slug}))
        return redirect(reverse('catalog:list'))
    return render(request, 'product/edit.html', {'form': form})


def product_del(request, product_slug):
    product = Product.objects.get(slug=str(product_slug))

    if request.method == 'POST':
        product = Product.objects.get(slug=str(product_slug))
        product.delete()
        return redirect(reverse('catalog:list'))
    else:
        product = Product.objects.get(slug=str(product_slug))
        return render(request, 'product/del.html', {'product': product})

    return render(request, 'product/del.html', {})
