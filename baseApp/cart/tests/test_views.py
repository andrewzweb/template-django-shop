from django.test import TestCase


class CartTest(TestCase):
    
    def test_can_create_cart(self):
        resp = self.client.get('/cart/')
        assert resp.status_code == 200

    def test_default_cart_empty(self):
        resp = self.client.get('/cart/')
        assert 'Cart is empty...' in resp

