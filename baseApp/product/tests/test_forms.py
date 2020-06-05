from django.test import TestCase
from product.models import Product, Category
from product.forms import ProductForm


class ProductFormTest(TestCase):
    ''' product test '''

    def test_form_add_product(self):
        ''' test form add product '''
        ProductForm({'title': 'product1'}).save()
        assert Product.objects.count() == 1

    def test_product_add_categoty(self):
        ''' test form product add category '''
        category = Category.objects.create(title='title').save()
        ProductForm({'title': 'product1', 'category': category}).save()
        assert Product.objects.first().category == category
