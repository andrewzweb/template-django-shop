from django.test import TestCase
from django.urls import  reverse
from product.urls import *
from product.forms import AddProductForm

class AddProductFormTest(TestCase):
    ''' add product tests'''

    def test_form_add_product(self):
        assert Product.objects.count() == 0
        form = AddProductForm({'title':'product1'})
        form.save()
        assert Product.objects.count() == 1
