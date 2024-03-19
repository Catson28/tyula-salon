from rest_framework import serializers
from .models import Category, CategoryImage
from apps.image.models import Image
# from apps.image.serializers import ImagesSerializer  # Importe o serializer de imagem aqui

class CategorySerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    def get_images(self, obj):
        images_queryset = CategoryImage.objects.filter(category=obj)
        images_serializer = ImagesSerializer(images_queryset, many=True)
        return images_serializer.data

    class Meta:
        model = Category
        fields = ["id", "name", "description", "images"]


class ImagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"


class ImagesSerializer(serializers.ModelSerializer):
    image = ImagSerializer(read_only=True)
    class Meta:
        model = CategoryImage
        fields = ["id", "image"]
