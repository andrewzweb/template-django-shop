from django.test import TestCase
from django.utils.text import slugify
from django.urls import reverse
from product.models import Product, Category
from django.utils.datastructures import MultiValueDictKeyError


class HomePageTest(TestCase):
    ''' home page '''
    def test_get_home_page(self):
        get_home_page = self.client.get('/')
        assert get_home_page.status_code == 200


class ProductItemTest(TestCase):
    ''' product item '''

    def test_get_item(self):
        product_name = 'some product'
        Product.objects.create(title=product_name)
        product_url = slugify(product_name)
        resp = self.client.get(reverse('catalog:item', args=(product_url,)))
        assert resp.status_code == 200

    def test_default_products_item_dont_exist(self):
        assert Product.objects.count() == 0


class AddProductTest(TestCase):
    ''' add product tests'''

    product_data = {'title': 'product1', 'price': 123}
    product_data_2 = {'title': 'product2', 'price': 123}
    product_data_3 = {'title': 'product3', 'price': 123}

    def test_add_product(self):
        ''' test add product '''
        self.client.post(reverse('catalog:product_add'), {'title': 'product1', 'price': 2})
        assert Product.objects.count() == 1


    def NO_test_add_product_without_price_fail(self):
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

    def test_add_product(self):
        ''' test can add product '''
        resp = self.client.post(reverse('catalog:product_add'), self.product_data)
        assert Product.objects.count() == 1

        
    def NOtest_cant_add_product_with_the_same_title(self):
        ''' test add product with the same title '''
        add_first_product = self.client.post(reverse('catalog:product_add'), self.product_data)
        add_second_product = self.client.post(reverse('catalog:product_add'), self.product_data)
        self.assertContains(add_second_product, 'Product with this Title already exists')
        assert add_second_product.status_code == 302


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
        ''' test edit product change price '''
        p_title = 'product'
        p_price_fisrt = 2
        p_price_second = 3
        Product.objects.create(title=p_title, price=p_price_fisrt).save()
        self.client.post(
            reverse('catalog:product_edit', kwargs={'product_slug': p_title}),
            {
                'title': p_title,
                'price': p_price_second
            })
        assert '3.00' in str(Product.objects.first().price)

    def test_edit_product_clear_price(self):
        ''' test esit clear price '''
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
    ''' delete product '''

    def test_delete_product_send_POST(self):
        ''' test delete product '''
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

    def test_when_delete_need_confirm(self):
        ''' test when delete need confirm  '''
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


class TestCategoryView(TestCase):
    ''' category test '''

    def test_filter_list_by_category(self):
        ''' test filter list by category '''
        category = Category.objects.create(title='category2')
        prod1 = Product.objects.create(title='prod1', category=category)
        prod2 = Product.objects.create(title='prod2', category=category)
        prod3 = Product.objects.create(title='prod3')
        assert Product.objects.count() == 3

        resp = self.client.get(reverse('catalog:filter_by_category',
                                       kwargs={'category_slug': 'category2'}))
        self.assertContains(resp, prod1)
        self.assertContains(resp, prod2)
        self.assertNotContains(resp, prod3.title)

    def FIX_test_add_category_to_product(self):
        ''' test add category to product '''
        p_title = 'product'
        category = Category.objects.create(title='category2')
        Product.objects.create(title=p_title).save()
        self.client.post(
            reverse('catalog:product_edit', kwargs={'product_slug': p_title}),
            {
                'title': p_title,
                'category': category.pk
            })
        assert Product.objects.count() == 1
        assert category.title == Product.objects.first().category


