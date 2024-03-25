from rest_framework import serializers
from .models import Seller, InvoiceCategory, Invoice, InvoiceItem, InvoicePayment, SoldItem, ProvidedService, ProvidedServiceEnpl

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ['id', 'type', 'person']  # Incluindo todos os campos do modelo Seller

class InvoiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceCategory
        fields = ['id', 'name']  # Incluindo todos os campos do modelo InvoiceCategory

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['id', 'invoice_number', 'issuance_date', 'due_date', 'payment_type', 'total_amount', 'seller', 'client', 'category']

class InvoiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceItem
        fields = ['id', 'description', 'quantity', 'unit_price', 'line_total', 'invoice']  # Incluindo todos os campos do modelo InvoiceItem

class InvoicePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoicePayment
        fields = ['id', 'payment_date', 'amount_paid', 'invoice']  # Incluindo todos os campos do modelo InvoicePayment

class SoldItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoldItem
        fields = ['id', 'quantity', 'invoice', 'product']  # Incluindo todos os campos do modelo SoldItem

class ProvidedServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProvidedService
        fields = ['id', 'service_date_duration', 'alternative_price', 'total_service_value', 'invoice', 'service']  # Incluindo todos os campos do modelo ProvidedService

class ProvidedServiceEnplSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProvidedServiceEnpl
        fields = ['id', 'employee', 'provided_service']  # Incluindo todos os campos do modelo ProvidedServiceEnpl










