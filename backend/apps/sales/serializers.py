from rest_framework import serializers
from .models import Seller, InvoiceCategory, Invoice, InvoiceItem, InvoicePayment, SoldItem, ProvidedService, ProvidedServiceEnpl
from apps.employee.serializers import EmployeeSerializer
from apps.service.serializers import ServiceSerializer
from apps.product.serializers import ProductSerializer
from apps.customer.serializers import CustomerSerializer
from apps.person.serializers import PersonSerializer

class SellerSerializer(serializers.ModelSerializer):
    person = PersonSerializer(read_only=True)
    class Meta:
        model = Seller
        fields = ['id', 'type', 'person']  # Incluindo todos os campos do modelo Seller

class InvoiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceCategory
        fields = ['id', 'name']  # Incluindo todos os campos do modelo InvoiceCategory

class InvoiceSerializer(serializers.ModelSerializer):
    category = InvoiceCategorySerializer(read_only=True)
    seller = SellerSerializer(read_only=True)
    client = CustomerSerializer(read_only=True)
    class Meta:
        model = Invoice
        fields = ['id', 'invoice_number', 'issuance_date', 'due_date', 'payment_type', 'total_amount', 'seller', 'client', 'category']

class InvoiceItemSerializer(serializers.ModelSerializer):
    invoice = InvoiceSerializer(read_only=True)
    class Meta:
        model = InvoiceItem
        fields = ['id', 'description', 'quantity', 'unit_price', 'line_total', 'invoice']  # Incluindo todos os campos do modelo InvoiceItem

class InvoicePaymentSerializer(serializers.ModelSerializer):
    invoice = InvoiceSerializer(read_only=True)
    class Meta:
        model = InvoicePayment
        fields = ['id', 'payment_date', 'amount_paid', 'invoice']  # Incluindo todos os campos do modelo InvoicePayment

class SoldItemSerializer(serializers.ModelSerializer):
    invoice = InvoiceSerializer(read_only=True)
    product = ProductSerializer(read_only=True)
    class Meta:
        model = SoldItem
        fields = ['id', 'quantity', 'invoice', 'product']  # Incluindo todos os campos do modelo SoldItem

class ProvidedServiceSerializer(serializers.ModelSerializer):
    invoice = InvoiceSerializer(read_only=True)
    service = ServiceSerializer(read_only=True)
    class Meta:
        model = ProvidedService
        fields = ['id', 'service_date_duration', 'alternative_price', 'total_service_value', 'invoice', 'service']  # Incluindo todos os campos do modelo ProvidedService

class ProvidedServiceEnplSerializer(serializers.ModelSerializer):
    provided_service = ProvidedServiceSerializer(read_only=True)
    employee = EmployeeSerializer(read_only=True)
    class Meta:
        model = ProvidedServiceEnpl
        fields = ['id', 'employee', 'provided_service']  # Incluindo todos os campos do modelo ProvidedServiceEnpl










