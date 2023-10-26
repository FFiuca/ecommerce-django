from django.test import TestCase
from rest_framework.test import APITestCase, force_authenticate, APIClient
from store.factories.storeFactory import BootFactory
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from user.models import Customer
from store import models as sModel
from order import models as mOrder
from master import models as mMaster
from user.factories import BootFactory as BootFactoryUser
import json

class CartTest(APITestCase):
    fixtures= ['status', 'usertype']

    def setUp(self) -> None:
        BootFactoryUser.runCustomerFactory()
        BootFactory.runStoreFactory(3)
        BootFactory.runTagFactory()

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

class CheckOutTest(APITestCase):
    fixtures = ['status', 'usertype', 'payment_status', 'payment_method']

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

        self.setUp()

    def setUp(self) -> None:
        BootFactoryUser.runCustomerFactory()
        BootFactory.runStoreFactory(3)
        BootFactory.runTagFactory()
        BootFactory.runItemStoreFactory(1)

        self.user = Customer.objects.first().user

        self.client = APIClient()

        self.client.login(username=self.user.username, password='1234')

    # @classmethod
    def test_add_checkout(self):
        item = sModel.ItemStore.objects.first()

        data = {
            'data': {
                'payment_method': mMaster.PaymentMethod.objects.first().pk,
                'user_store': item.store_id,
            },
            'item': [
                {
                    'item' : item.item_id,
                    'qty' : 100,
                }
            ]
        }
        data = json.dumps(data)

        req = self.client.post(reverse('order:checkout-add'), data=data, content_type='application/json')
        req = req.json()

        print(req)

        self.assertEqual(req['status'], 200)
        
        return req


class PaymentTest(APITestCase):
    fixtures = ['status', 'usertype', 'payment_status', 'payment_method']

    def setUp(self) -> None:
        super().setUp()

        BootFactoryUser.runCustomerFactory()
        BootFactory.runStoreFactory(3)
        BootFactory.runTagFactory()
        BootFactory.runItemStoreFactory(1)
        BootFactoryUser.makeAdminFactory()

        self.customer = Customer.objects.first()
        self.admin = User.objects.filter(is_staff=1).first()

        self.client = APIClient()
        self.client.login(username=self.admin.username, password='1234')

        self.checkout_test = CheckOutTest()

    def test_change_paymnent_status(self):

        # it's better not call other test in current test, can use functions class directly
        co = self.checkout_test.test_add_checkout()

        # print(type(co))
        # assert if co is success
        self.assertEqual(co['status'], 200)

        co = co['data']['co']
        print('cp2', co)
        data = {
            'checkout_code': co['checkout_code'],
            'payment_status': 3,
        }

        req = self.client.post(reverse('order:payment.change_payment_status'), data=data)
        req = req.json()
        print(req)

        self.assertEqual(req['status'], 200)
