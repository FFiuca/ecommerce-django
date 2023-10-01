from factory import django
from store import models as sModel
from master import models as mModel
from faker import Faker
from user import factories as fUser
from user import models as mUser
from master import factories as fMaster
import factory
from main.fakerHelper import FakerHelper

fake = Faker(['id_ID'])
fakeHelper = FakerHelper().fake

class StoreFactory(django.DjangoModelFactory):
    class Meta:
        model = sModel.UserStore
        django_get_or_create = ['store_name',]

    store_name = factory.Sequence(lambda n: 'store {}'.format(n))
    owner = factory.SubFactory(fUser.OwnerAndUserFactory)
    status = mModel.Status.objects.filter(module_name='store.user_store', status_int=1).get()

class ItemFactory(django.DjangoModelFactory):
    class Meta:
        model = sModel.UserItem
        django_get_or_create = ('item_name', 'owner', )

    item_name = factory.LazyAttribute(lambda el: fakeHelper.ecommerce_name())
    owner = factory.SubFactory(fUser.OwnerAndUserFactory)
    # category = factory.SubFactory(factory=fMaster.CategoryFactory)

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        print(create, extracted) # maybe create determine he action is create, and extracted determine get from db for get_or_create behaviour
        if not create or not extracted:
            return

        self.category.add(*extracted)

class TagFactory(django.DjangoModelFactory):
    class Meta:
        model = sModel.UserTag
        django_get_or_create = ('tag_name', 'owner',)

    tag_name = factory.LazyAttribute(lambda el: fakeHelper.text(max_nb_chars=20))
    owner = factory.SubFactory(fUser.OwnerAndUserFactory)

    @factory.post_generation
    def item(self, create, extracted, **kwargs):
        if not create or not extracted:
            return

        self.item.add(*extracted)


class BootFactory:
    @classmethod
    def runStoreFactory(self, size=1):
        # a = StoreFactory(owner=mUser.OwnerAndUser.objects.first())
        # a = StoreFactory.create_batch(size or 1, owner=mUser.OwnerAndUser.objects.first())
        a = StoreFactory.create_batch(size or 1)

        print(a)

    @classmethod
    def runItemFactory(self, size_category: None|int =None, size_item: None|int =None):
        c = fMaster.CategoryFactory.create_batch(size_category or 1)
        # a = ItemFactory(category=[c])
        a = ItemFactory.create_batch(size_item or 1, category=c)

        print(a)
        return a

    @classmethod
    def runTagFactory(self):
        item = self.runItemFactory(size_category=2, size_item=3)

        tag = TagFactory.create_batch(10, item=item)

        print(tag)

