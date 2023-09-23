from rest_framework.test import APITestCase
from faker import Faker
from django.urls import reverse

fake = Faker(['id_ID'])
class RegisterTest(APITestCase):
    fixtures = ['status', 'usertype'] # run the seeder

    def test_register(self):
        username = fake.user_name()
        password = username
        email = fake.email()

        data = {
            'username': username,
            'password': password,
            'password2': password,
            'email' : email,
            'customer_name': fake.name(),
            'mobile_phone': fake.phone_number(),
        }

        response = self.client.post(reverse('user:register-list'), data)
        json = response.json()
        print(json)
        self.assertEqual(json['status'], 200)

    def test_register_owner(self):
        username = fake.user_name()
        password = username
        email = fake.email()

        data = {
            'username': username,
            'password': password,
            'password2': password,
            'email': email,
            'owner_name': fake.name(),
            'mobile_phone': fake.phone_number()
        }

        response = self.client.post(reverse('user:register-owner-list'), data)
        json = response.json()
        print(json)
        self.assertEqual(json['status'], 200)
