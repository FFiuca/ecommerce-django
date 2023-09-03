import factory
from user import models
from faker import Faker
from master.models import Status, UserType
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

faker = Faker()

class UserFactory(factory.Factory):
    class Meta:
        model = User

    username = factory.Faker('user_name')
    password = factory.LazyFunction(lambda username=username: make_password('1234'))
    email = factory.Faker('email')
    is_superuser = factory.LazyFunction(lambda: faker.random_element(elements=(1,0,)))
    is_staff = factory.LazyFunction(lambda: faker.random_element(elements=(1,0,)))

class CustomerFactory(factory.Factory):
    class Meta:
        model = models.Customer

    mobile_phone = factory.Faker('phone_number')
    customer_name = factory.Faker('name')
    email = factory.Faker('email')
    status = Status.objects.filter(module_name='user.customer', status_int=1).order_by('?').first() # to get randomly
    usertype = UserType.objects.get(pk=1)
    user = factory.SubFactory(UserFactory)

class BootFactory:
    def runCustomerFactory(self):
        for x in range(10):
            a = CustomerFactory()
            a.user.save()
            a.save()



