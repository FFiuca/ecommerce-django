import factory
from master import models
from faker import Faker
import faker_commerce

fake = Faker()
fake.add_provider(faker_commerce.Provider)

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Category
        django_get_or_create = ('category_name',)

    category_name = factory.Sequence(lambda el: fake.ecommerce_category())
