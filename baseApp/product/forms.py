from django import forms
from product.models import Product


class ProductForm(forms.ModelForm):
    ''' product form '''

    class Meta:
        model = Product
        fields = ('image', 'category', 'title', 'price',)
