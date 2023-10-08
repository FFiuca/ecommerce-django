from rest_framework import serializers
from order.models import Cart
from user.api.serializers import CustomerSerializer
from store.api.serializers.ItemSerializers import ItemSerializer

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        exclude = []

    customer = CustomerSerializer(many=False, read_only=True)
    item = ItemSerializer(many=False, read_only=True)
