from django.test import TestCase
from django.urls import reverse
from account.views import * 

class AccountTest(TestCase):

    def test_get_profile_page(self):
        resp = self.client.get(reverse('account:detail'))
        self.assertContains(resp, 'Hi') 
        self.assertContains(resp, 'You account') 

