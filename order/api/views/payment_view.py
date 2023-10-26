from rest_framework import viewsets, views, mixins, generics
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response
from django.forms import ValidationError
from main import helpers

from order.api.forms import payment_forms
from order.api.functions import payment_functions

# APIView can't use as_view method in urls
class PaymentView(viewsets.ViewSet):
    permission_classes= [IsAdminUser]

    @action(methods=['POST'], detail=False)
    def change_payment_status(self, request, *args, **kwargs):
        result = None
        valid = None
        try:
            checkout_code = request.data.get('checkout_code')
            payment_status = request.data.get('payment_status')

            valid = payment_forms.UpdatePaymentStatusForm({
                'checkout_code': checkout_code,
                'payment_status': payment_status,
            })

            if valid.is_valid() is False:
                raise ValidationError('Form Error')
            
            # print( 'aa', valid.cleaned_data['payment_status'].pk)

            # class() need () to not pass self param if want call method directly
            result = payment_functions.PaymentFunctions().change_payment_status(
                                                checkout_code=valid.cleaned_data['checkout_code'], 
                                                status=valid.cleaned_data['payment_status'].pk # due ModelChoiceField validtion forms, return object of class model
                                                )
        except ValidationError as e:
            return Response(data={
                'status': 400,
                'data': {
                    'error': valid.errors
                }
            })
        except Exception as e:
            return Response(data={
                'status': 500,
                'data': {
                    'error': helpers.messageError(e)
                }
            })

        return Response(data={
            'status': 200,
            'data': result
        }, status=200)




