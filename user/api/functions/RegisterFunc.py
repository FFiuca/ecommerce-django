from user.api.serializers import UserSerializer, CustomerSerializer
from master.models import UserType, Status
from django.contrib.auth.models import User
from user.models import Customer, OwnerAndUser
from django.core import serializers
from django.forms.models import model_to_dict

class RegisterCustomer():
    def create(self, dataUser, dataCustomer):
        dUser = {**dataUser}

        # del dUser['password']
        del dUser['password2']

        # user = User(**dUser)
        # user = User(username='caco', email='email@email.com', password='passw')

        # user.set_password('passw')
        # user = user.save()
        user = User.objects.create_user(**dUser)
        # print('user', user, dUser)
        if user is None:
            raise Exception('Error create user')

        dataCustomer['status'] = Status.objects.filter(module_name='user.customer', status_name='active').get()
        dataCustomer['usertype'] = UserType.objects.get(pk=1)
        dataCustomer['user'] = user

        print('cust', dataCustomer)
        # customer = CustomerSerializer(data=dataCustomer)
        # customer.is_valid()
        customer = Customer.objects.create(**dataCustomer)
        print(customer)

        # customer = customer.save()
        if customer is None:
            raise Exception('Error create customer')

        return {
            'user' : user.pk,
            'customer': customer.pk
        }

class RegisterOwner():
    def create(self, data_user, data_owner):
        del data_user['password2']

        user = User.objects.create_user(**data_user)

        if user is None:
            raise Exception('Error create user')

        data_owner['status'] = Status.objects.filter(module_name='user.owner', status_name='active').get()
        data_owner['usertype'] = UserType.objects.get(pk=2)
        data_owner['user'] = user

        owner = OwnerAndUser.objects.create(**data_owner)
        if owner is None:
            raise Exception('Error create owner')

        return {
            'user': model_to_dict( user), # to convert single model to dict
            'customer': model_to_dict(owner),
            # 'user': list(user) / user.values() # to convert many model to list
        }
