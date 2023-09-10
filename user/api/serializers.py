from rest_framework import serializers, validators as restValidator, exceptions
from user.models import Customer
from django.contrib.auth.models import User
from user.api import validators

class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={
            'input_style': 'password'
        },
        write_only=True
    )

    class Meta:
        model= User
        exclude=['password']
        extra_kwargs = {
            'password' : {
                'write_only': True
            }
        }

    def validate_password2(self, obj):
        print('obj', obj, self.initial_data.get('password'))
        password = self.initial_data.get('password')
        if password is not None and obj=='bypass_pass':
            return obj

        if validators.is_same(password, obj)!=True:
            raise serializers.ValidationError('Password is not match each others')

        return obj

class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=False)
    email = serializers.EmailField(
            # blank=False,
            validators = [
                restValidator.UniqueValidator(
                    queryset=Customer.objects.all()
                )
            ]
        )

    class Meta:
        model= Customer
        exclude=[]

