import os
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver 
from selenium.common.exceptions import WebDriverException
import time 

from product.models import Product
from django.utils.text import slugify

MAX_WAIT = 7

class FunctionalTest(StaticLiveServerTestCase):
    """ base for functional tests """

    def setUp(self):
        ''' start firefox '''
        self.browser = webdriver.Firefox()
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server: 
            self.live_server_url = 'http://' + staging_server

    def tearDown(self):
        ''' quit from browser'''
        self.browser.quit()

    def get_item_input_box(self):
        '''get input element'''
        return self.browser.find_element_by_id('id_text')


    def wait(fn):
        ''' wait str in table '''

        def modified_fn(*args,**kwargs):
            start_time = time.time()
            while True:
                try: 
                    return fn(*args,**kwargs)
                except (AssertionError, WebDriverException) as e:
                    if time.time() - start_time > MAX_WAIT:
                        raise e
                    time.sleep(0.5)
        return modified_fn

    @wait
    def wait_for(self, fn):
        return fn


    def add_product(self, name=None):
        if name == None:
            name_of_product = 'product1'
        else: 
            name_of_product = str(name)

        p1 = Product.objects.create(title=name_of_product)
        p1.save()
        slug_name_product = slugify(name_of_product)
        return slug_name_product

