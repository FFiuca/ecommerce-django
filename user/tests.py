from rest_framework.test import APITestCase
from faker import Faker
from django.urls import reverse
from user.api.functions import RegisterFunc

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

class LoginTest(APITestCase):
    fixtures = ['status', 'usertype']

    def test_login_customer(self):
        username = fake.user_name()
        password = username
        email = fake.email()
        # email = 'caco@gmail.com'
        customer_name = fake.name(),
        phone = fake.phone_number()

        user = {
            'username': username,
            'password': password,
            'password2': password,
            'email': email,
            'is_active': 1,
            'is_staff': 0,
            'is_superuser': 0,
        }

        customer = {
            'email': email,
            'customer_name': customer_name,
            'mobile_phone': phone,
        }

        create = RegisterFunc.RegisterCustomer.create(self, dataUser=user, dataCustomer=customer)
        print('crt', create)
        login = {
            'email': email,
            'password': password,
        }

        response = self.client.post(reverse('user:login-customer'), login)
        response = response.json()
        print(response)
        self.assertEqual(response['status'], 200)

    def test_login_owner(self):
        username = fake.user_name()
        password = username
        email = fake.email()
        # email = 'caco@gmail.com'
        owner_name = fake.name(),
        phone = fake.phone_number()

        user = {
            'username': username,
            'password': password,
            'password2': password,
            'email': email,
            'is_active': 1,
            'is_staff': 0,
            'is_superuser': 0,
        }

        owner = {
            'email': email,
            'owner_name': owner_name,
            'mobile_phone': phone,
        }

        create = RegisterFunc.RegisterOwner.create(self, user, owner)
        print('crt', create)
        login = {
            'email': email,
            'password': password,
        }

        response = self.client.post(reverse('user:login-owner'), login)
        response = response.json()
        print(response)
        self.assertEqual(response['status'], 200)




