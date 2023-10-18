from rest_framework import views, viewsets, generics, mixins
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from drf_nested_field_multipart import NestedMultipartParser
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
    parser_classes=[FormParser, MultiPartParser, JSONParser]

    # @action(detail=False, methods=['POST'])
    def add(self, request, *args, **kwargs):
        valid = None
        add = None
        try:
            print(request.data)
            data = request.data.get('data')
            item = request.data.get('item')

            validation_data = {
                **data,
                'item': item
            }

            valid = checkout_forms.AddCheckoutForm(data=validation_data)
            if valid.is_valid() is False:
                raise ValidationError('validation error')
            # print(request.user.customer)
            add = checkout_functions.CheckOutFunctions(request.user.customer)
            print(data, item)
            add = add.add(data, item)

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
            'status': 200,
            'data': add
        }, status=200)
