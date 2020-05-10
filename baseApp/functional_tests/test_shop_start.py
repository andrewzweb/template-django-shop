from .base import FunctionalTest
import time 

class ShopShowStartPageTest(FunctionalTest):

    def test_get_start_page_and_check_title(self):
        '''get start page '''

        self.browser.get(self.live_server_url)
        self.assertIn('Shop', self.browser.title)


    def test_simple_page_has_main_element(self):
        '''get start page '''

        self.browser.get(self.live_server_url)
        self.assertIn('Shop', self.browser.title)

        self.browser.find_element_by_id('header')
        self.browser.find_element_by_id('products')
        self.browser.find_element_by_id('footer')


    def test_get_catalog_product_page(self):
        self.add_product_in_catalog()
        self.browser.get(self.live_server_url+'/catalog/')
        products = self.browser.find_elements_by_class_name('product-item')
        assert len(products) == 2
        

