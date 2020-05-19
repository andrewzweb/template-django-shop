from django.test import TestCase
from django.conf import settings
from unittest import skip
from django.urls import reverse 
from product.models import Product

class CartTest(TestCase):
    
    def test_can_go_to_url_cart(self):
        resp = self.client.get('/cart/')
        assert resp.status_code == 200

    def test_default_cart_empty(self):
        resp = self.client.get('/cart/')
        self.assertContains(resp, "Cart is empty" )


class CartInSessionTest(TestCase):

    def test__add_session(self):
        resp = self.client.get('/cart/')
        session = self.client.session
        assert session.keys() == {'cart':[]}.keys()

    
    def test_add_item_in_cart(self):
        product = Product.objects.create(title='avokado')
        assert Product.objects.count() == 1
        
        # cart empty 
        resp1 = self.client.get(reverse('cart:cart_detail'))
        self.assertContains(resp1, 'empty')

        # add to cart 
        add = self.client.post(reverse('cart:cart_add',kwargs={'product_id': product.id}))

        # now cart must full
        resp2 = self.client.get(reverse('cart:cart_detail'))
        #self.assertNotContains(resp2, 'empty')
        self.assertContains(resp2, '1')

