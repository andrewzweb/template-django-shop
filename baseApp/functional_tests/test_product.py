from .base import FunctionalTest
from django.urls import reverse
from product.models import Product


class ProductItemTest(FunctionalTest):
    ''' test product item'''

    def test_get_product_item(self):
        ''' get product '''

        # create product
        slug_name = self.add_product(name='product1')

        # get_product
        self.get_page(reverse('catalog:item', kwargs={'product_slug':slug_name}))

        # see title
        assert slug_name in self.wait_for(self.browser.find_element_by_class_name('product__title').text)

    def test_get_dont_exist_product(self):
        ''' get dont exist product '''

        # Samanta input wrong url
        self.get_page('/product/dont-exist/')

        # and see
        assert str('Not Found') in self.browser.page_source

class AddProductTest(FunctionalTest):
    ''' test add product item'''

    def test_add_product_item(self):
        ''' get product item '''

        # Samanta want add product ot shop
        # product params was
        product_name = 'product1'
        product_price = 1

        # Samanta go to add_product page
        self.get_page(reverse('catalog:product_add'))

        # see in page 'Add product'
        assert 'Add product' in self.browser.page_source

        # find field title
        find_title_field = self.wait_for(self.browser.find_element_by_name("title").clear())
        # typing a name of product what we want add
        self.browser.find_element_by_name("title").send_keys(product_name)

        # find price field
        find_price_field= self.wait_for(self.browser.find_element_by_name('price').clear())
        # typing a price of product what we want add 
        self.browser.find_element_by_name('price').send_keys(product_price)

        # click to submit  
        find_submit = self.browser.find_element_by_name('add').click()

        # when browser redirect to main page and can see title
        assert product_name in self.browser.find_element_by_class_name('product__title').text
        # and price
        assert str(product_price) in self.browser.find_element_by_class_name('product__price').text


class EditProductTest(FunctionalTest):
    ''' test edit product item'''

    def test_edit_product_item(self):
        ''' test edit product item '''

        # create item
        Product.objects.create(title='product', price=1)

        # Samanta want edit product and change title and price
        # product params was
        new_product_name = str('product1')
        new_product_price = int(3)

        # Samanto go to home page
        self.get_page(reverse('catalog:list'))

        # she see product and clict to view product
        self.wait_for(self.browser.find_element_by_link_text('view detail')).click()

        # she see link Edit and click
        self.wait_for(self.browser.find_element_by_link_text('Edit')).click()

        # find field title and change title
        self.wait_for(self.browser.find_element_by_name("title").clear())
        # typing a name of product what we want add
        self.browser.find_element_by_name("title").send_keys(new_product_name)

        # find price field and change title
        self.wait_for(self.browser.find_element_by_name('price').clear())
        # typing a price of product what we want add
        self.browser.find_element_by_name('price').send_keys(new_product_price)

        # click to submit
        find_submit = self.browser.find_element_by_name('add').click()

        # when browser redirect to main page and can see  new title
        assert new_product_name in self.browser.find_element_by_class_name('product__title').text
        # and price
        assert str(new_product_price) in self.browser.find_element_by_class_name('product__price').text


class DelProductTest(FunctionalTest):
    ''' test edit product item'''

    def test_del_product_item(self):
        ''' test delete product item '''

        # create item
        Product.objects.create(title='product', price=1)

        # Samanta want del old product

        # Samanto go to home page
        self.get_page(reverse('catalog:list'))

        # she see product and clict to view product
        self.wait_for(self.browser.find_element_by_link_text('view detail')).click()

        # she see link Delete and click
        self.wait_for(self.browser.find_element_by_link_text('Delete')).click()

        # Title page  delete
        assert 'Delete' in  self.browser.title

        # and Samanta confirm action delete item
        self.browser.find_element_by_name('delete').click()
        

        # when browser redirect to main page and can see  new title
        assert len(self.browser.find_elements_by_class_name('product__title')) == 0
        # and price
        assert len(self.browser.find_elements_by_class_name('product__price')) == 0
