from django.urls import path
from .views import *

app_name="product"

urlpatterns = [
    path('<slug:slug>/', product_item, name='item'),
    path('', product_list, name='list'),
]

