from django.test import TestCase
from django.urls import reverse
from account.views import * 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model 

UserModel = get_user_model()

class AccountTest(TestCase):

    def test_get_profile_page(self):
        resp = self.client.get(reverse('account:detail'))
        self.assertContains(resp, 'Hi') 
        self.assertContains(resp, 'You account') 
        self.assertContains(resp, 'login') 


class LoginAccountTest(TestCase):

    def test_login_user_exist(self):
        username = 'john'
        email = 'lennon@thebeatles.com'
        password = 'johnpassword'
        user = User.objects.create_user(username, email, password)
        assert self.client.login(username=username, password=password) == True

    def test_no_login_user_dont_exist(self):
        assert self.client.login(username='fake', password='pass') == False

    def test_no_login_user_dont_exist(self):
        register = self.client.post(
            reverse('account:register'), 
            {'usename': 'test', 'password': 'awesome'}
        )
        assert register.status_code == 200
        

class RegisterTest(TestCase):

    def test_registration_user_can_get(self):
        assert self.client.get(reverse('account:register')).status_code == 200 

    def test_registration_done_exist(self):
        assert self.client.get(reverse('account:register-done')).status_code == 200
        
    def test_registration(self):
        
        register = self.client.post(
            reverse('account:register'), 
            {
            'usename': 'test', 
            'email': 'awesome@mail.com',
            'password1': 'awesome',
            'password2': 'awesome',
            }
        )
        #assert UserModel.objects.count() == 1
        pass

    def test_registration_without_email(self):
        register = self.client.post(
            reverse('account:register'), 
            {
            'usename': 'test', 
            'password1': 'awesome',
            'password2': 'awesome',
            }
        )
        #assert register.status_code == 302
        assert User.objects.count() == 0



        
