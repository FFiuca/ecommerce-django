from django import forms
from master import models as mMaster

def check_valid_co_code(val):
    if not val.startswith('CO') :
        raise forms.ValidationError('Not valid checkout code')

    return True

class UpdatePaymentStatusForm(forms.Form):
    payment_status = forms.ModelChoiceField(required=True, queryset=mMaster.PaymentStatus.objects.all(),
                                            empty_label=None)
    checkout_code = forms.CharField(
        required=True,
        validators=[
            check_valid_co_code
        ],
        )
