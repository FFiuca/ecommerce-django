from rest_framework import views, viewsets, generics, mixins
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from order.api.serializers.cart_serializer import CartSerializer
from order import models
from order.api.functions import cart_functions


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
