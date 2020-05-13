from django.test import TestCase


class CartTest(TestCase):
    
    def test_can_create_cart(self):
        resp = self.client.get('/cart/')
        assert resp.status_code == 200

    def test_default_cart_empty(self):
        resp = self.client.get('/cart/')
        self.assertContains(resp, "Cart is empty" )

    def test_add_item_in_cart(self):
        cart_item = CartItem.objects.create(title='Avocado',count=2,price=float(2.00))
        resp = self.client.get('/cart/')
        self.assertNotContains(resp, "Cart is empty")
        self.assertIn(cart_item, resp)


