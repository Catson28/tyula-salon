from rest_framework import serializers
from .models import Subcategory
from apps.category.serializers import CategorySerializer


class SubcategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Subcategory
        fields = ["id", "name", "description", "category"]
