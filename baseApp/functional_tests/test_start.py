from .base import FunctionalTest
from django.urls import reverse


class ShopShowStartPageTest(FunctionalTest):

    def test_get_start_page_and_check_title(self):
        '''get start page '''
        self.browser.get(self.live_server_url)

        self.wait_for(self.browser.find_element_by_id('header'))
        self.wait_for(self.browser.find_element_by_id('footer'))

        self.assertIn('Catalog', self.browser.title)

    def test_get_catalog_product_page(self):
        ''' test get catalog product page'''
        self.add_product(name='one')
        self.add_product(name='two')

        self.browser.get(self.live_server_url)
        products = self.wait_for(self.browser.find_elements_by_class_name('product-item'))
        assert len(products) == 2
