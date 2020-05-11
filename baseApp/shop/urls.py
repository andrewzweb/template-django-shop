from django.urls import path, include
from shop import views as  shop_view

urlpatterns = [
    path('', shop_view.home, name='shop_index'),
    path('catalog/', include('product.urls', namespace='product')),
]


