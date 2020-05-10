from django.urls import path, include
from shop import views as  shop_view

urlpatterns = [
    path('', shop_view.home),
    path('catalog/', include('product.urls')),
]


