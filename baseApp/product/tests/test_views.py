from django.test import TestCase
from django.utils.text import slugify
from django.urls import  reverse
from product.models import Product
from product.urls import *

class HomePageTest(TestCase):

    def test_get_home_page(self):
        get_home_page = self.client.get('/')
        assert get_home_page.status_code == 200 

    
class ProductItemTest(TestCase):
    
    def test_get_item(self):
        product_title = 'product item #111'
        create_product = Product.objects.create(title=product_title)
        product_url = slugify(product_title)
        get_product_page = self.client.get(reverse('catalog:item', args=(product_url,))) 
        assert get_product_page.status_code == 200


class ProductAddTest(TestCase):
    ''' test add product'''
    
    product_data = {'title': 'product1', 'price': 123}
    product_data_2 = {'title': 'product2', 'price': 123}
    product_data_3 = {'title': 'product3', 'price': 123}

    def test_add_product(self):
        ''' test can add product '''
        resp = self.client.post(reverse('catalog:add'), self.product_data) 
        assert Product.objects.count() == 1

    def test_after_add_product_redirect(self):
        ''' test after add product redirect '''
        add_product = self.client.post(reverse('catalog:add'), self.product_data) 
        assert add_product.status_code == 302

    def test_cant_add_product_with_the_same_title(self):
        ''' test add product with the same title '''
        add_first_product = self.client.post(reverse('catalog:add'), self.product_data) 
        add_second_product = self.client.post(reverse('catalog:add'), self.product_data) 
        self.assertContains(add_second_product, 'Product with this Title already exists')
        assert add_second_product.status_code == 200

    def test_add_many_products(self):
        ''' test add more one product '''
        add_first_product = self.client.post(reverse('catalog:add'), self.product_data) 
        assert Product.objects.count() == 1

        add_second_product = self.client.post(reverse('catalog:add'), self.product_data_2) 
        assert Product.objects.count() == 2

        add_third_product = self.client.post(reverse('catalog:add'), self.product_data_3) 
        assert Product.objects.count() == 3

        
        


