from rest_framework import serializers
from store import models as sModel

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = sModel.UserTag
        exclude = []

