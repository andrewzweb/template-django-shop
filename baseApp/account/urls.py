from django.urls import path
from . import views

app_name="account"

urlpatterns = [
    path('', views.detail, name='detail'),
    path('login/', views.account_login, name='login'),
    path('logout/', views.account_logout, name='logout'),
]

