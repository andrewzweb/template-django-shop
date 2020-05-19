from .base import FunctionalTest
from django.urls import reverse
from product.models import Product
import time

class ProductItemTest(FunctionalTest):
    ''' test product item'''

    def test_get_product_item(self):
        ''' get product item '''
        
        slug_name = self.add_product(name='product1')
        self.browser.get(self.live_server_url + reverse('catalog:list', kwargs={'product_slug':slug_name}))
        self.assertIn('Shop', self.browser.title)


