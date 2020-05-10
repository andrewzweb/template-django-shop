import os
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver 
from selenium.common.exceptions import WebDriverException
import time 

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
