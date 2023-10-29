from rest_framework import views, viewsets, generics, mixins
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from order.api.serializers.cart_serializer import CartSerializer
from order import models
from order.api.functions import cart_functions
from order.api.forms import cart_forms
from django.http import request as dj_request
from asgiref.sync import async_to_sync, sync_to_async
from django.views import View


class CartView(viewsets.ModelViewSet):
    serializer_class= CartSerializer
    queryset = models.Cart.objects.by_current_user().all()
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['POST'])
    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer
        query = self.get_queryset()
        data = request.data

        result = cart_functions.CartFunctions.list(self, serializer, query, data)

        return Response(data=result, status=result['status'])

    @action(detail=False, methods=['POST'])
    def add(self, request, *args, **kwargs):
        query = self.get_queryset()
        data = request.data.get('data')

        valid = cart_forms.AddCartForm(data=data)
        if valid.is_valid() is False:
            return Response(data={
                'status': 402,
                'data': valid.errors
            })

        result = cart_functions.CartFunctions.add_to_cart(self, query, data)

        return Response(data=result, status=result['status'])


class AsyncCartView(View):
    # serializer_class= CartSerializer
    # queryset = models.Cart.objects.by_current_user().all()
    # permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['GET'])
    async def get(self, request, *args, **kwargs):
        # serializer = CartSerializer
        # query = models.Cart.objects.by_current_user().all()
        # data = await request.data

        result = await async_to_sync( self.get_data())
        result = result.values()

        return Response(data=result, status=200)

    async def get_data(self, data=None):
        query = await models.Cart.objects.by_current_user().afirst()

        return query
