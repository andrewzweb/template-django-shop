from django.urls import path
from shop import views as  shop_view

urlpatterns = [
    path('', shop_view.home, name='shop_index'),
]


