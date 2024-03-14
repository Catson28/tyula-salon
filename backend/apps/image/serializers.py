from rest_framework import serializers
from .models import Image, ServiceImage, Product
from apps.service.models import Service
from apps.product.models import Product


class ServiceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceImage
        fields = ["service", "image"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["product", "image"]


# class ImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Image
#         fields = ['ImageID', 'Path', 'content_type', 'object_id', 'content_object']


class ImageSerializer(serializers.ModelSerializer):
    # Use serializers.ImageField para campos de upload de arquivos
    Path = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Image
        fields = ["ImageID", "Path", "content_type", "object_id", "content_object"]
