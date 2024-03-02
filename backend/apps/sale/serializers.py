from rest_framework import serializers
from .models import Sale, ClientSale, ProductSale

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ['id', 'products', 'professional', 'customer', 'payment_type', 'date_time', 'alternative_price']

class ClientSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientSale
        fields = ['client', 'sale']

class ProductSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSale
        fields = ['product', 'sale']
