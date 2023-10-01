from django.test import TestCase
from rest_framework.test import APITestCase
from store.factories.storeFactory import BootFactory
from django.urls import reverse

class ItemTest(APITestCase):
    fixtures= ['status', 'usertype']

    def setUp(self) -> None:
        BootFactory.runStoreFactory(3)
        # BootFactory.runItemFactory(size_item=5)
        BootFactory.runTagFactory()

    def test_search_item(self):
        res = self.client.post(reverse('store:item.list'))
        res = res.json()

        self.assertEqual(res['status'], 200)


