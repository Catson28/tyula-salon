from rest_framework import serializers
from .models import Image, ServiceImage
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


'''
# serializers.py
from rest_framework import serializers
from .models import Image, ServiceImage, ProductImage, CategoryImage

class ServiceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceImage
        fields = ["service", "image"]

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["product", "image"]


class ImageSerializer(serializers.ModelSerializer):
    Path = serializers.CharField(source='image_path')  # Substitua 'image_path' pelo nome correto do campo que armazena o caminho da imagem
    class Meta:
        model = Image
        fields = ["ImageID", "Path", "content_type", "object_id", "content_object"]

class CategoryImageSerializer(serializers.ModelSerializer):
    image = ImageSerializer()  # Certifique-se de referenciar o serializer correto para o campo de imagem
    class Meta:
        model = CategoryImage
        fields = ["category", "image"]




'''