from django.urls import path
from .views import *

app_name="catalog"

urlpatterns = [
    path('', product_list, name='list'),
    path('<slug:product_slug>/', product_item, name='item'),
]

