from rest_framework import viewsets, views, mixins, generics
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response
from django.forms import ValidationError
from main import helpers

from order.api.forms import payment_forms
from order.api.functions import payment_functions

class PaymentView(views.APIView):
    permission_classes= [IsAdminUser]

    @action(methods=['POST'], detail=False)
    def change_payment_status(self, request, *args, **kwargs):
        result = None
        valid = None
        try:
            checkout_code = request.data.get('checkout_code')
            status = request.data.get('status')

            valid = payment_forms.UpdatePaymentStatusForm({
                'checkout_code': checkout_code,
                'status': status,
            })

            if valid.is_valid() is False:
                raise ValidationError('Form Error')

        except ValidationError as e:
            return Response(data={
                'code': 400,
                'data': {
                    'error': valid.errors
                }
            })
        except Exception as e:
            return Response(data={
                'code': 500,
                'data': {
                    'error': helpers.messageError(e)
                }
            })

        return Response(data={
            'code': 200,
            'data': result
        }, status=200)




