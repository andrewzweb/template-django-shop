from django.shortcuts import render
from product.models import Product, Category


def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'shop/base.html', locals())
