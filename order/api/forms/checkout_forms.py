from django import forms
from django.core import validators
from order import models
from main import validator_helpers

class ItemsCheckOutValidator(forms.Field):
    def __init__(self, min_value=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # it will be provide min_value prop to compare with qty. See parent class
        # if digging deeper can use @deconstructible to make own validators and support flexibility
        self.min_value = min_value


    def validate(self, value) -> None:
        super().validate(value)

        if not isinstance(value, list):
            raise forms.ValidationError('Item must be a list.')

        if not all(isinstance(item, dict) for item in value):
            raise forms.ValidationError('Each element in the list must be dict.')

        for item in value:
            if ('item', 'qty',) in item is False:
                raise forms.ValidationError('Structure dict is not meet the requirement.')

            validator_helpers.RequiredValidator(val= item.get('item'), field_name='Item')
            min_value_validator = validators.MinValueValidator(self.min_value)
            min_value_validator(item['qty'])




class AddCheckoutForm(forms.Form):
    class Meta:
        model = models.Checkout
        fields =[
            'customer',
            'user_store',
            'payment_method'
        ]

    item = ItemsCheckOutValidator(min_value=1)

