from django.test import TestCase
from django.contrib.auth.models import User


class UserTest(TestCase):
    ''' user test '''

    def test_can_create_default_user_model(self):
        user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        user.last_name = 'Lennon'
        user.save()
        assert User.objects.count() == 1
    

    def test_auth_some_user(self):
        pass
        
