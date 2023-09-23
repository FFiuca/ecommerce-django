from user.models import Customer, OwnerAndUser
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password
from user.api.exceptions import PasswordInvalidException, AccountInactive
from django.core.exceptions import ObjectDoesNotExist

class LoginFunc():

    def login_customer(self, data: dict):
        email = data['email']
        password = data['password']

        print('email', email)

        owner = Customer.objects.filter(email=email).get()
        if owner is None:
            raise ObjectDoesNotExist()

        user = owner.user
        status = owner.status

        if check_password(password, user.password) is False:
            raise PasswordInvalidException()

        if status.status_name=='inactive' or user.is_active is 0:
            raise AccountInactive()

        token = RefreshToken.for_user(user)

        data = {
            'token': str(token.access_token),
            'refresh_token': str(token)
        }

        return data

    def login_owner(self, data:dict):
        email = data['email']
        password = data['password']

        print('email', email)

        owner = OwnerAndUser.objects.filter(email=email).get()
        if owner is None:
            raise ObjectDoesNotExist()

        user = owner.user
        status = owner.status

        if check_password(password, user.password) is False:
            raise PasswordInvalidException()

        if status.status_name=='inactive' or user.is_active is 0:
            raise AccountInactive()

        token = RefreshToken.for_user(user)

        data = {
            'token': str(token.access_token),
            'refresh_token': str(token)
        }

        return data
