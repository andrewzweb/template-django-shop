from django.test import TestCase
from django.utils.text import slugify
from django.urls import  reverse
from product.models import Product
from product.urls import *

class HomePageTest(TestCase):
    
    def test_get_home_page(self):
        resp = self.client.get('/')
        assert resp.status_code == 200 

    
class ProductItemTest(TestCase):
    
    def test_get_item(self):
        product_name = 'some product'
        product_item = Product.objects.create(title=product_name)
        product_url = slugify(product_name)
        resp = self.client.get(reverse('catalog:item', args=(product_url,))) 
        assert resp.status_code == 200

class AddProductTest(TestCase):
    ''' add product tests'''

    def test_add_product_post(self):
        assert Product.objects.count() == 0
        self.client.post(reverse('catalog:product_add'), {'title':'producsdf', 'price':2})
        assert Product.objects.count() == 1

    def test_add_two_products(self):
        assert Product.objects.count() == 0
        self.client.post(reverse('catalog:product_add'), {'title':'produc1', 'price':2})
        assert Product.objects.count() == 1
        self.client.post(reverse('catalog:product_add'), {'title':'product2', 'price':2})
        assert Product.objects.count() == 2


