from rest_framework import views, viewsets, generics, mixins
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django.forms import ValidationError

from order import models as mOrder
from order.api.serializers import checkout_serializer
from main import helpers
from order.api.forms import checkout_forms
from order.api.functions import checkout_functions

class CheckOutView(viewsets.ModelViewSet):
    serializer_class = checkout_serializer.CheckOutSerializer
    queryset = mOrder.Checkout.objects.all()
    permission_classes=[IsAuthenticated]

    def add(self, request, *args, **kwargs):
        valid = None
        add = None
        try:
            data = request.data.get('data')
            item = request.data.get('item')

            validation_data = {
                **data,
                'item': item
            }

            valid = checkout_forms.AddCheckoutForm(data=validation_data)
            if valid.is_valid() is False:
                raise ValidationError('validation error')

            add = checkout_functions.CheckOutFunctions.add(self, data, item)
        except ValidationError as e:
            return Response(data={
                'status': 400,
                'data': {
                    'error' : valid.errors
                }
            }, status=400)
        except Exception as e:
            return Response(data={
                'status': 500,
                'data': {
                    'error': helpers.messageError(e)
                }
            }, status=500)

        return Response(data={
            'code': 200,
            'data': add
        }, status=200)
