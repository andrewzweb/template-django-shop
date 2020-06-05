from django.forms import ModelForm
from product.models import Product


class ProductForm(ModelForm):
    ''' product form '''
    class Meta:
        model = Product
        fields = ('image', 'category', 'title', 'price',)
