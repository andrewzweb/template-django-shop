from django.test import TestCase
from django.urls import reverse
from account.views import * 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


class AccountTest(TestCase):

    def test_get_profile_page(self):
        resp = self.client.get(reverse('account:detail'))
        self.assertContains(resp, 'Hi') 
        self.assertContains(resp, 'You account') 
        self.assertContains(resp, 'login') 

    def test_login_user_exist(self):
        username = 'john'
        email = 'lennon@thebeatles.com'
        password = 'johnpassword'
        user = User.objects.create_user(username, email, password)
        #user.save()
        assert self.client.login(username=username, password=password) == True

    def test_login_user_dont_exist(self):
        assert self.client.login(username='fake', password='pass') == False

        



        
