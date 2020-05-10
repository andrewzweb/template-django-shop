from .base import FunctionalTest

class ShopShowStartPageTest(FunctionalTest):

    def test_get_start_page(self):
        '''get start page '''

        self.browser.get(self.live_server_url)
        self.assertIn('Shop', self.browser.title)

