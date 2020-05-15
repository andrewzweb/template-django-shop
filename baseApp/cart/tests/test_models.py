from django.test import TestCase
from cart.models import * 

class CartModelTest(TestCase):
    cart = Cart.objects.create()
    cart_item = CartItem.objects.create(title='Avocado',count=2,price=float(2.00))
    
    
