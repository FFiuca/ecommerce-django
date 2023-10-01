from rest_framework import serializers
from store import models as sModel
from master.api.serializers import categorySerializer
from store.api.serializers import tagSerializer

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = sModel.UserItem
        exclude = []

    category = categorySerializer.CategorySerializer(read_only=True, many=True)
    user_tag_item = tagSerializer.TagSerializer(read_only=True, many=True) # must match with related_name

