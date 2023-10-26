from django import forms
from master import models as mMaster

def check_valid_co_code(val):
    if not val.startswith('CO') :
        raise forms.ValidationError('Not valid checkout code')

    return True

class UpdatePaymentStatusForm(forms.Form):
    payment_status = forms.IntegerField(required=True)
    checkout_code = forms.ModelChoiceField(
        required=True,
        choices=mMaster.PaymentStatus.objects.all(),
        validators=[
            check_valid_co_code
        ],
        empty_label=None
        )
