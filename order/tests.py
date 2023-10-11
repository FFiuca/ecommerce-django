from django.test import TestCase
from rest_framework.test import APITestCase, force_authenticate, APIClient
from store.factories.storeFactory import BootFactory
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from user.models import Customer
from store import models as sModel
from user.factories import BootFactory as BootFactoryUser

class CartTest(APITestCase):
    fixtures= ['status', 'usertype']

    def setUp(self) -> None:
        BootFactoryUser.runCustomerFactory()
        BootFactory.runStoreFactory(3)
        BootFactory.runTagFactory()

        print('ckck')
        self.user = Customer.objects.first().user

        self.client = APIClient()
        self.client.login(username=self.user.username, password='1234')

    def test_cart_list(self):
        print(self.user)
        req = self.client.post(reverse('order:cart-list'), data={
            'item': 1
        })
        req = req.json()

        self.assertEqual(req['status'], 200)

    def test_add_to_cart(self):
        item = sModel.UserItem.objects.first()

        data = {
            'data' : {
                'item': item.pk,
                'qty': 1,
            }
        }

        req = self.client.post(reverse('order:cart-add'), data=data, format='json')
        req = req.json()
        print(req)
        self.assertEqual(req['status'], 200)


