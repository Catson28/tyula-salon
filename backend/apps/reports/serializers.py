from rest_framework import serializers
from .models import SalesReport, BillingReport, FrequentCustomersReport, InventoryReport

class SalesReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesReport
        fields = ['id', 'Sale_Date', 'customer', 'Total_Sale']  # Incluindo todos os campos do modelo SalesReport

class BillingReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingReport
        fields = ['id', 'Period', 'Total_Invoices_Issued', 'Total_Invoices_Paid', 'Total_Invoices_Pending']  # Incluindo todos os campos do modelo BillingReport

class FrequentCustomersReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrequentCustomersReport
        fields = ['id', 'customer', 'Num_Purchases', 'Total_Purchase_Value']  # Incluindo todos os campos do modelo FrequentCustomersReport

class InventoryReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryReport
        fields = ['id', 'Available_Products', 'Quantity_Sold', 'Replenishment_Quantity', 'Low_Stock_Alerts']  # Incluindo todos os campos do modelo InventoryReport
