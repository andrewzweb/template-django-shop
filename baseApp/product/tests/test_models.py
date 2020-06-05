from django.test import TestCase
from product.models import Product, Category
from django.db.utils import IntegrityError


class ProductTest(TestCase):
    ''' product test '''

    def test_create_product(self):
        Product.objects.create(title='title')
        assert Product.objects.count() == 1

    def test_slug_auto_change_on_title(self):
        ''' test slug auto change on title'''
        Product.objects.create(title='title')
        assert 'title' == Product.objects.first().slug

    def test__cant_create_product_with_same_title(self):
        ''' test cant create product with same title '''
        Product.objects.create(title='title')
        with self.assertRaises(IntegrityError):
            Product.objects.create(title='title')


class CategoryTest(TestCase):
    ''' category test '''

    def test_can_create_category(self):
        ''' test create category'''
        Category.objects.create(title='title')
        assert Category.objects.count() == 1

    def test_cant_create_category_with_same_title(self):
        ''' test cant create category with same title '''
        Category.objects.create(title='title')
        with self.assertRaises(IntegrityError):
            Category.objects.create(title='title')

    def test_can_create_couple_categories(self):
        ''' test can create couple categories '''
        Category.objects.create(title='title1')
        Category.objects.create(title='title2')
        Category.objects.create(title='title3')
        assert Category.objects.count() == 3

    def test_add_category_to_product(self):
        ''' test add category to product '''
        category = Category.objects.create(title='title')
        product = Product.objects.create(title='title', category=category)
        assert product.category == category

    def test_add_same_category_to_different_product(self):
        ''' test add same category to different product '''
        category = Category.objects.create(title='title').save()
        Product.objects.create(title='title', category=category)
        Product.objects.create(title='title2', category=category)
        assert Product.objects.count() == 2
        assert len(Product.objects.filter(category__id=category)) == 2

    def test_add_different_category_to_different_product(self):
        ''' test add different category to different product '''
        category_first = Category.objects.create(title='first').save()
        category_second = Category.objects.create(title='second').save()
        Product.objects.create(title='title', category=category_first)
        Product.objects.create(title='title2', category=category_second)
        assert Product.objects.count() == 2
        assert Product.objects.first().category == category_first
        assert Product.objects.last().category == category_second 
