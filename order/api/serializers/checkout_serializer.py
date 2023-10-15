from rest_framework import serializers
from order import models as mOrder
from store.api.serializers.ItemSerializers import ItemSerializer

class CheckOutDetailSerializer(serializers.ModelSerializer):
    class Meta :
        model = mOrder.CheckoutDetail
        exclude = []

    item = ItemSerializer(many=False, read_only=True)

class CheckOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = mOrder.Checkout
        exclude = []

    checkout_detail = CheckOutDetailSerializer(many=True, read_only=True)


