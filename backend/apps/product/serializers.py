from rest_framework import serializers
from .models import Product 
from apps.image.models import Image, ProductImage
from apps.image.serializers import ImageSerializer


class ProductSerializer(serializers.ModelSerializer):


    images = serializers.SerializerMethodField()
    cover = serializers.SerializerMethodField()
    # products = serializers.SerializerMethodField() # ProductSerializer((many=True, read_only=True)

    def get_images(self, obj):
        images_queryset = ProductImage.objects.filter(product=obj)
        images_serializer = ImagesSerializer(images_queryset, many=True)
        return images_serializer.data

    def get_cover(self, obj):
        # Filtra as ProductImages pelo campo "cover" igual a True
        cover_image = ProductImage.objects.filter(product=obj, cover=True).last()
        if cover_image:
            # return cover_image.image.ImageID  # Retorna o ID da imagem de capa
            return ImageSerializer(cover_image.image).data  # Retorna os dados completos da imagem de capa
        return None  # Retorna None se nenhuma imagem de capa for encontrada
    class Meta:
        model = Product
        fields = ["id", "name", "cost", "description", "quantity", "category", "cover", "unit_price", "images"]


class ImagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"


class ImagesSerializer(serializers.ModelSerializer):
    image = ImagSerializer(read_only=True)
    class Meta:
        model = ProductImage
        fields = ["id", "image", "cover"]