from rest_framework import mixins, viewsets, generics
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from django.contrib.auth.models import User
from user.api.serializers import UserSerializer, CustomerSerializer
from master.models import UserType, Status
from user.api.functions.RegisterFunc import RegisterCustomer, RegisterOwner
from main.helpers import messageError
from user.api import forms as formsUser
from django import forms

class RegisterView(mixins.CreateModelMixin, viewsets.ViewSet):

    def create(self, request, *args, **kwargs):
        userS = None
        customerS = None
        add = None
        form = None

        data = request.data
        try:
            print(data, data['username'])

            user = {
                'username': data['username'],
                'password': data['password'],
                'password2': data['password2'],
                'email': data['email'],
                'is_active': 1,
                'is_staff': 0,
                'is_superuser': 0,
            }

            customer = {
                'email': data['email'],
                'customer_name': data['customer_name'],
                'mobile_phone': data['mobile_phone'],
                # 'status': Status.objects.filter(module_name='user.customer', status_name='active').get().pk,
                # 'usertype': UserType.objects.get(pk=1).pk,
                # 'user': User.objects.create_user(username='caco', password='11', email='email@e.com'),
            }

            form = formsUser.RegisterForm(data=data)
            if form.is_valid() is False:
                raise forms.ValidationError('validation error')

            # print(customer)

            # userS = UserSerializer(data=user)
            # customerS = CustomerSerializer(data=customer)
            # # print('aa',userS.is_valid(), customerS.is_valid(), userS.errors, user)
            # if userS.is_valid()!=True or customerS.is_valid()!=True:
            #     raise ValidationError()

            # user['password2'] = 'bypass_pass'

            add = RegisterCustomer.create(self, user, customer)

        except forms.ValidationError as e:
            return Response(data={
                'status': 400,
                'data': {
                    'error' : {
                        # **userS.errors,
                        # **customerS.errors
                        **form.errors
                    }
                }
            }, status=400)
        except Exception as e:
            return Response(data={
                'status': 500,
                'data': {
                    'error' : messageError(e)
                }
            }, status=500)

        return Response(data={
            'status': 200,
            'data': add
        }, status=200)


class RegisterOwnerView(mixins.CreateModelMixin, viewsets.ViewSet):

    def create(self, request, *args, **kwargs):
        userS = None
        customerS = None
        add = None
        form = None

        data = request.data
        # print('hh', data)
        try:
            form = formsUser.RegisterOwnerForm(data=data)
            if form.is_valid()==False:
                raise forms.ValidationError('validation error')


            user = {
                'username': data['username'],
                'password': data['password'],
                'password2': data['password2'],
                'email': data['email'],
                'is_active': 1,
                'is_staff': 0,
                'is_superuser': 0
            }

            owner = {
                'email': data['email'],
                'owner_name': data['owner_name'],
                'mobile_phone': data['mobile_phone'],
            }

            add = RegisterOwner.create(self, data_user=user, data_owner=owner)

        except forms.ValidationError as e:
            return Response(data={
                'status': 400,
                'data': {
                    'error' : ''
                }
            }, status=400)
        except Exception as e:
            return Response(data={
                'status': 500,
                'data': {
                    'error': messageError(e)
                }
            }, status=500)


        return Response(data={
            'status': 200,
            'data': add
        }, status=200)














