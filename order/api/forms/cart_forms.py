from django import forms
from order import models

class AddCartForm(forms.Form):
    class Meta:
        model = models.Cart
        fields = [
            # 'customer',
            'item',
            'qty'
        ]
