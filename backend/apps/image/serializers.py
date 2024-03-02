from rest_framework import serializers
from .models import Image, ProductImage, RawMaterialImage
from apps.product.models import Product
from apps.material.models import RawMaterial

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['product', 'image']

class RawMaterialImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawMaterialImage
        fields = ['raw_material', 'image']

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['ImageID', 'Path', 'content_type', 'object_id', 'content_object']
