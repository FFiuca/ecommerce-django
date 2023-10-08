from django.test import TestCase
from rest_framework.test import APITestCase, force_authenticate, APIClient
from store.factories.storeFactory import BootFactory
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from user.models import Customer
from user.factories import BootFactory as BootFactoryUser

class CartTest(APITestCase):
    fixtures= ['status', 'usertype']

    def setUp(self) -> None:
        BootFactoryUser.runCustomerFactory()
        BootFactory.runStoreFactory(3)
        BootFactory.runTagFactory()

        print('ckck')
        self.user = Customer.objects.first().user

    def test_cart_list(self):
        client = APIClient()
        client.login(username=self.user.username, password='1234')
        print(self.user)
        req = client.post(reverse('order:cart-list'), data={
            'item': 1
        })
        req = req.json()

        self.assertEqual(req['status'], 200)

