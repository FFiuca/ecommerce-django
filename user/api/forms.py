from django import forms
from user.api import validators

class RegisterForm(forms.Form):
    username = forms.CharField(required=True, max_length=50)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
    password2 = forms.CharField(required=True)
    customer_name = forms.CharField(required=True)
    mobile_phone = forms.CharField(required=True)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if validators.is_same(password1, password2) is False:
            raise forms.ValidationError('Password not match', code='Invalid')

        return password2

class RegisterOwnerForm(forms.Form):
    username = forms.CharField(required=True, max_length=50)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
    password2 = forms.CharField(required=True)
    owner_name = forms.CharField(required=True)
    mobile_phone = forms.CharField(required=True)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        print(password1, password2)
        if password1 != password2:
            raise forms.ValidationError('Password not match', code='Invalid')

        return password2
