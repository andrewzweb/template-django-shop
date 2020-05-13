from django.urls import path
from .views import *

app_name="catalog"

urlpatterns = [
    path('all/', product_list, name='list'),
    path('item/<slug:product_slug>/', product_item, name='item'),
]

