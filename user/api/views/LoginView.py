from rest_framework import mixins, viewsets, views
from rest_framework.response import Response
from django.forms import ValidationError
from user.api import forms
from rest_framework.decorators import action
from master import models
from main.helpers import messageError
from user.api.functions import LoginFunc
from user.api.exceptions import PasswordInvalidException, AccountInactive
from django.core.exceptions import ObjectDoesNotExist

class LoginView(viewsets.ViewSet):

    @action(detail=False, methods='POST')
    def login_customer(self, request):
        data = request.data

        try:
            data = data.copy() # to convert into dict

            # data = {
            #     'email': data['email'],
            #     'password': data['password']
            # }

            valid = forms.LoginForm(data=data)

            if valid.is_valid() is False:
                raise ValidationError('validation error')

            data = LoginFunc.LoginFunc.login_customer(self, data)

        except ValidationError as e:

            return Response(data={
                'status': 400,
                'data': {
                    'error': data.errors,
                    'tt': e.error_list
                }
            })
        except (ObjectDoesNotExist, PasswordInvalidException, AccountInactive) as e:
            return Response(data={
                'status': 403,
                'data': {
                    'error': messageError(e)
                }
            })
        except Exception as e:
            return Response(data={
                'status': 500,
                'data': {
                    'error': messageError(e)
                }
            })

        return Response(data={
            'status': 200,
            'data': data
        })

    @action(detail=False, methods='POST')
    def login_owner(self, request):
        data = request.data

        try:
            data = data.copy() # to convert into dict

            # data = {
            #     'email': data['email'],
            #     'password': data['password']
            # }

            valid = forms.LoginForm(data=data)

            if valid.is_valid() is False:
                raise ValidationError('validation error')

            data = LoginFunc.LoginFunc.login_owner(self, data)

        except ValidationError as e:

            return Response(data={
                'status': 400,
                'data': {
                    'error': data.errors,
                    'tt': e.error_list
                }
            })
        except (ObjectDoesNotExist, PasswordInvalidException, AccountInactive) as e:
            return Response(data={
                'status': 403,
                'data': {
                    'error': messageError(e)
                }
            })
        except Exception as e:
            return Response(data={
                'status': 500,
                'data': {
                    'error': messageError(e)
                }
            })

        return Response(data={
            'status': 200,
            'data': data
        })

