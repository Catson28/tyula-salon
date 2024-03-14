from rest_framework import serializers
from .models import Sale, ClientSale, ServiceSale


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = [
            "id",
            "services",
            "professional",
            "customer",
            "payment_type",
            "date_time",
            "alternative_price",
        ]


class ClientSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientSale
        fields = ["client", "sale"]


class ServiceSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceSale
        fields = ["service", "sale"]
