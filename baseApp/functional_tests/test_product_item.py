from .base import FunctionalTest
from django.urls import reverse

class ProductItemTest(FunctionalTest):
    ''' test product item'''

    def test_get_product_item(self):
        ''' get product item '''
        
        slug_name = self.add_product(name='product1')
        self.browser.get(self.live_server_url + reverse('catalog:item', kwargs={'product_slug':slug_name}))
        self.wait_for(self.browser.find_elements_by_class_name('product-item')) 


