from .base import FunctionalTest

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

