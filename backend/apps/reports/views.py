from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SalesReportSerializer, BillingReportSerializer, FrequentCustomersReportSerializer, InventoryReportSerializer
from .models import SalesReport, BillingReport, FrequentCustomersReport, InventoryReport
from rest_framework.views import APIView
from .models import SalesReport, BillingReport, FrequentCustomersReport, InventoryReport
from .serializers import (
    SalesReportSerializer,
    BillingReportSerializer,
    FrequentCustomersReportSerializer,
    InventoryReportSerializer,
)
from django.shortcuts import get_object_or_404


@api_view(['GET'])
def sales_report_list(request):
    sales_reports = SalesReport.objects.all()
    serializer = SalesReportSerializer(sales_reports, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def billing_report_list(request):
    billing_reports = BillingReport.objects.all()
    serializer = BillingReportSerializer(billing_reports, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def frequent_customers_report_list(request):
    frequent_customers_reports = FrequentCustomersReport.objects.all()
    serializer = FrequentCustomersReportSerializer(frequent_customers_reports, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def inventory_report_list(request):
    inventory_reports = InventoryReport.objects.all()
    serializer = InventoryReportSerializer(inventory_reports, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_sales_report(request):
    serializer = SalesReportSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_billing_report(request):
    serializer = BillingReportSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_frequent_customers_report(request):
    serializer = FrequentCustomersReportSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_inventory_report(request):
    serializer = InventoryReportSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SalesReportDetailView(APIView):
    def get(self, request, pk):
        sales_report = get_object_or_404(SalesReport, pk=pk)
        serializer = SalesReportSerializer(sales_report)
        return Response(serializer.data)

class BillingReportDetailView(APIView):
    def get(self, request, pk):
        billing_report = get_object_or_404(BillingReport, pk=pk)
        serializer = BillingReportSerializer(billing_report)
        return Response(serializer.data)

class FrequentCustomersReportDetailView(APIView):
    def get(self, request, pk):
        frequent_customers_report = get_object_or_404(FrequentCustomersReport, pk=pk)
        serializer = FrequentCustomersReportSerializer(frequent_customers_report)
        return Response(serializer.data)

class InventoryReportDetailView(APIView):
    def get(self, request, pk):
        inventory_report = get_object_or_404(InventoryReport, pk=pk)
        serializer = InventoryReportSerializer(inventory_report)
        return Response(serializer.data)
