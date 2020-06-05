from django.urls import path
from . import views

app_name = "catalog"

urlpatterns = [
    path('', views.product_list, name='list'),
    path('add/', views.product_add, name='product_add'),
    path('product/<slug:product_slug>', views.product_item, name='item'),
    path('product/<slug:product_slug>/edit', views.product_edit, name='product_edit'),
    path('product/<slug:product_slug>/delete', views.product_del, name='product_del'),
    path('category/<slug:category_slug>', views.product_list, name='filter_by_category'),
]
