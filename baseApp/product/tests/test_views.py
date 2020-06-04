from django.test import TestCase
from django.utils.text import slugify
from django.urls import reverse
from product.models import Product
from product.urls import *
from django.utils.datastructures import MultiValueDictKeyError


class HomePageTest(TestCase):
    ''' home page '''

    def test_get_home_page(self):
        ''' test get home page '''
        resp = self.client.get('/')
        assert resp.status_code == 200


class ProductItemTest(TestCase):
    ''' product item '''

    def test_get_item(self):
        product_name = 'some product'
        product_item = Product.objects.create(title=product_name)
        product_url = slugify(product_name)
        resp = self.client.get(reverse('catalog:item', args=(product_url,)))
        assert resp.status_code == 200

    def test_default_products_item_dont_exist(self):
        assert Product.objects.count() == 0


class AddProductTest(TestCase):
    ''' add product tests'''

    def test_add_product(self):
        ''' test add product '''
        self.client.post(reverse('catalog:product_add'), {'title': 'product1', 'price': 2})
        assert Product.objects.count() == 1

    def test_add_product_without_price_fail(self):
        ''' test add product without price fail '''
        with self.assertRaises(MultiValueDictKeyError):
            self.client.post(reverse('catalog:product_add'), {'title': 'produc1'})
        assert Product.objects.count() == 0

    def test_add_two_products(self):
        ''' test add two products '''
        self.client.post(reverse('catalog:product_add'), {'title': 'p1', 'price': 2})
        assert Product.objects.count() == 1
        self.client.post(reverse('catalog:product_add'), {'title': 'p2', 'price': 2})
        assert Product.objects.count() == 2


class EditProductTest(TestCase):
    ''' add product tests'''

    def test_edit_product_change_title(self):
        ''' test edit product change title '''
        p_title_first = 'product'
        p_title_second = 'product'
        p_price = 2
        Product.objects.create(title=p_title_first, price=p_price)

        self.client.post(
            reverse('catalog:product_edit', kwargs={'product_slug': p_title_first}),
            {
                'title': p_title_second,
                'price': p_price
            })
        assert Product.objects.first().title == p_title_second

    def test_edit_product_change_price(self):
        p_title='product'
        p_price_fisrt = 2
        p_price_second = 3
        Product.objects.create(title=p_title, price=p_price_fisrt)

        self.client.post(
            reverse('catalog:product_edit', kwargs={'product_slug': p_title}),
            {
                'title': p_title,
                'price': p_price_second
            })

        assert Product.objects.first().price == p_price_second

    def test_edit_product_clear_price(self):
        p_title = 'product'
        p_price = 2
        Product.objects.create(title=p_title, price=p_price)

        self.client.post(
            reverse('catalog:product_edit', kwargs={'product_slug': p_title}),
            {
                'title': p_title,
                'price': ''
            })

        assert Product.objects.first().price == None


class DeleteProductTest(TestCase):
    ''' del product tests'''

    def test_delete_product_send_POST(self):
        p_title = 'product'
        p_price = 2
        Product.objects.create(title=p_title, price=p_price)
        assert Product.objects.count() == 1

        response = self.client.post(
            reverse('catalog:product_del', kwargs={'product_slug': p_title}),
            {
                'title': p_title,
            })
        assert response.status_code == 302
        assert Product.objects.count() == 0

    def test_delete_product_send_GET(self):
        p_title = 'product'
        p_price = 2
        Product.objects.create(title=p_title, price=p_price)
        assert Product.objects.count() == 1

        response = self.client.get(
            reverse('catalog:product_del', kwargs={'product_slug': p_title}),
            {
                'title': p_title,
            })
        assert response.status_code == 200
        assert b'delete' in response.content
