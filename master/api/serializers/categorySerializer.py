from rest_framework import serializers
from master import models

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        exclude = []
