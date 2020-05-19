from .base import FunctionalTest
from selenium.webdriver.support.ui import Select
from django.urls import reverse
from unittest import skip
import time 
import random 

class CartTest(FunctionalTest):
    ''' test cart '''

    def test_cart(self):
        ''' you see cart '''

        # add product
        self.add_product(name='product1', **{'price':2})

        # Toni go to our site  
        self.browser.get(self.live_server_url + reverse('catalog:list'))
        # He find link to cart and click
        link_to_cart = self.wait_for(self.browser.find_element_by_class_name('link-to-cart')).click()

        # And he see what cart is empty 
        self.wait_for(self.browser.find_element_by_xpath('//h2[text()="Cart is empty"]'))

        # Now he go to catalog
        self.wait_for(self.browser.find_element_by_xpath('//a[text()="Continue shopping"]')).click()
                      
        # He see to view in product
        products_view_link = self.wait_for(self.browser.find_elements_by_xpath('//a[text()="view detail"]'))
        assert len(products_view_link) == 1
        
        # Toni click to one of views-item
        random.choice(products_view_link).click()

        # He click to add in cart
        self.wait_for(self.browser.find_element_by_xpath('//button[text()="Add to cart"]')).click()
        
        # And we redirect to cart page and see item in cart list
        title = self.wait_for(self.browser.find_element_by_class_name('title-page')).text
        assert title == 'Your shopping cart'
        

        # And see red label near link to cart and he text equal qualuty items Toni add to cart  
        count_item_in_cart = self.wait_for(self.browser.find_element_by_class_name('count-item--exist')).text
        assert count_item_in_cart == '1'


class CartAddTest(FunctionalTest):
    ''' test cart '''

    def no_test_add_item_to_cart_from_page_catalog(self):
        ''' add product to cart '''
        pass 

    def test_add_item_to_cart_from_page_catalog_item(self):
        ''' add product to cart '''

        # add product
        slug = self.add_product(name='product1', **{'price':2})

        # Toni go to item page  
        self.browser.get(self.live_server_url + reverse('catalog:item', kwargs={'product_slug':slug,}))
        
        # He click to add in cart
        self.wait_for(self.browser.find_element_by_xpath('//button[text()="Add to cart"]')).click()
        

class CartChangesTest(FunctionalTest):
    ''' test cart '''

    def test_change_count_product_in_cart(self):
        ''' change count products in cart '''
        
        # add product
        slug = self.add_product(name='product1', **{'price':2})

        # Toni go to item page  
        self.browser.get(self.live_server_url + reverse('catalog:item', kwargs={'product_slug':slug,}))

        # He click to add in cart
        self.wait_for(self.browser.find_element_by_xpath('//button[text()="Add to cart"]')).click()
        
        # He want change count item in cart 
        ## Toni click to select field with count
        Select(self.browser.find_element_by_id('id_quantity')).select_by_value('3')

        ## click to update count 
        self.wait_for(self.browser.find_element_by_xpath("//input[@value='Update']").click())

        # Now Tone see option default is our choice 
        select_option = Select(self.browser.find_element_by_id('id_quantity')).first_selected_option
        assert select_option.text == '3'

        
    def test_delete_product_on_cart(self):
        ''' del product from cart '''

        # add product
        slug = self.add_product(name='product1', **{'price':2})

        # Toni go to item page  
        self.browser.get(self.live_server_url + reverse('catalog:item', kwargs={'product_slug':slug,}))

        # He click to add in cart
        self.wait_for(self.browser.find_element_by_xpath('//button[text()="Add to cart"]')).click()

        # Now Toni in cart and he delete item
        self.wait_for(self.browser.find_element_by_xpath('//a[text()="Remove"]')).click()
        
        # And he see what cart is empty 
        self.wait_for(self.browser.find_element_by_xpath('//h2[text()="Cart is empty"]'))


    def not_test_can_go_to_item_from_cart(self):
        ''' add product to cart '''
        pass

    def test_can_go_to_list_from_cart(self):
        ''' add product to cart '''

        # add product
        slug = self.add_product(name='product1', **{'price':2})

        # Toni go to item page  
        self.browser.get(self.live_server_url + reverse('catalog:item', kwargs={'product_slug':slug,}))

        # He click to add in cart
        self.wait_for(self.browser.find_element_by_xpath('//button[text()="Add to cart"]')).click()

        # Now he go to catalog
        self.wait_for(self.browser.find_element_by_xpath('//a[text()="Continue shopping"]')).click()

