from django.test import TestCase
from django.utils.text import slugify
from product.models import Product

class ProductTest(TestCase):

    def test_create_product(self):
        p = Product.objects.create(title='title')
        all = Product.objects.count()
        assert all > 0
        assert all == 1

    def test_after_craete_item_slug_create_to(self):
        name = 'title'
        create = Product.objects.create(title=name)
        item = Product.objects.first()
        assert item.slug == slugify(name) 




