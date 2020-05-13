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
        
