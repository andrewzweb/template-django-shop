from django.urls import path
from .views import *

app_name="catalog"

urlpatterns = [
    path('', product_list, name='list'),
    path('add/', product_add, name='product_add'),
    path('product/<slug:product_slug>/', product_item, name='item'),
]

