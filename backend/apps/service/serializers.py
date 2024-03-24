from rest_framework import serializers
from .models import Service, ServiceImage, ServiceProduct, FinancialAnalysis
from apps.image.models import Image
from apps.image.serializers import ImageSerializer
from apps.product.serializers import ProductSerializer


class ServiceProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceProduct
        fields = ["service", "product", "consume", "unit", "measurable", "status"]
        

class FinancialAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialAnalysis
        fields = ["cost", "liquid", "margin", "service", "business"]


# Importe o serializer de imagem aqui, se necessário

class ServiceSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    cover = serializers.SerializerMethodField()
    products = ProductSerializer(many=True, read_only=True)
    # products = serializers.SerializerMethodField() # ProductSerializer((many=True, read_only=True)

    def get_images(self, obj):
        images_queryset = ServiceImage.objects.filter(service=obj)
        images_serializer = ImagesSerializer(images_queryset, many=True)
        return images_serializer.data

    def get_cover(self, obj):
        # Filtra as ServiceImages pelo campo "cover" igual a True
        cover_image = ServiceImage.objects.filter(service=obj, cover=True).last()
        if cover_image:
            # return cover_image.image.ImageID  # Retorna o ID da imagem de capa
            return ImageSerializer(cover_image.image).data  # Retorna os dados completos da imagem de capa
        return None  # Retorna None se nenhuma imagem de capa for encontrada

    class Meta:
        model = Service
        fields = ["id", "name", "description", "price", "subcategory", "products", "images", "cover"]

class ImagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"


class ImagesSerializer(serializers.ModelSerializer):
    image = ImagSerializer(read_only=True)
    class Meta:
        model = ServiceImage
        fields = ["id", "image", "cover"]

