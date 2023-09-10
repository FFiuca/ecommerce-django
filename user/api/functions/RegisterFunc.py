from user.api.serializers import UserSerializer, CustomerSerializer
from master.models import UserType, Status
from django.contrib.auth.models import User
from user.models import Customer

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

