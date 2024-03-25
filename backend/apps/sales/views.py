from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Seller, InvoiceCategory, Invoice, InvoiceItem, InvoicePayment, SoldItem, ProvidedService, ProvidedServiceEnpl
from .serializers import SellerSerializer, InvoiceCategorySerializer, InvoiceSerializer, InvoiceItemSerializer, InvoicePaymentSerializer, SoldItemSerializer, ProvidedServiceSerializer, ProvidedServiceEnplSerializer
from .models import (
    Seller,
    InvoiceCategory,
    Invoice,
    InvoiceItem,
    InvoicePayment,
    SoldItem,
    ProvidedService,
    ProvidedServiceEnpl,
)
from .serializers import (
    SellerSerializer,
    InvoiceCategorySerializer,
    InvoiceSerializer,
    InvoiceItemSerializer,
    InvoicePaymentSerializer,
    SoldItemSerializer,
    ProvidedServiceSerializer,
    ProvidedServiceEnplSerializer,
)

@api_view(['GET'])
def seller_list(request):
    sellers = Seller.objects.all()
    serializer = SellerSerializer(sellers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def invoice_category_list(request):
    invoice_categories = InvoiceCategory.objects.all()
    serializer = InvoiceCategorySerializer(invoice_categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def invoice_list(request):
    invoices = Invoice.objects.all()
    serializer = InvoiceSerializer(invoices, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def invoice_item_list(request):
    invoice_items = InvoiceItem.objects.all()
    serializer = InvoiceItemSerializer(invoice_items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def invoice_payment_list(request):
    invoice_payments = InvoicePayment.objects.all()
    serializer = InvoicePaymentSerializer(invoice_payments, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def sold_item_list(request):
    sold_items = SoldItem.objects.all()
    serializer = SoldItemSerializer(sold_items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def provided_service_list(request):
    provided_services = ProvidedService.objects.all()
    serializer = ProvidedServiceSerializer(provided_services, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def provided_service_enpl_list(request):
    provided_services_enpl = ProvidedServiceEnpl.objects.all()
    serializer = ProvidedServiceEnplSerializer(provided_services_enpl, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def create_seller(request):
    serializer = SellerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_invoice_category(request):
    serializer = InvoiceCategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_invoice(request):
    serializer = InvoiceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_invoice_item(request):
    serializer = InvoiceItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_invoice_payment(request):
    serializer = InvoicePaymentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_sold_item(request):
    serializer = SoldItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_provided_service(request):
    serializer = ProvidedServiceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_provided_service_enpl(request):
    serializer = ProvidedServiceEnplSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import (
    Seller,
    InvoiceCategory,
    Invoice,
    InvoiceItem,
    InvoicePayment,
    SoldItem,
    ProvidedService,
    ProvidedServiceEnpl,
)
from .serializers import (
    SellerSerializer,
    InvoiceCategorySerializer,
    InvoiceSerializer,
    InvoiceItemSerializer,
    InvoicePaymentSerializer,
    SoldItemSerializer,
    ProvidedServiceSerializer,
    ProvidedServiceEnplSerializer,
)

class SellerDetailView(APIView):
    def get(self, request, pk):
        seller = get_object_or_404(Seller, pk=pk)
        serializer = SellerSerializer(seller)
        return Response(serializer.data)

class InvoiceCategoryDetailView(APIView):
    def get(self, request, pk):
        invoice_category = get_object_or_404(InvoiceCategory, pk=pk)
        serializer = InvoiceCategorySerializer(invoice_category)
        return Response(serializer.data)

class InvoiceDetailView(APIView):
    def get(self, request, pk):
        invoice = get_object_or_404(Invoice, pk=pk)
        serializer = InvoiceSerializer(invoice)
        return Response(serializer.data)

class InvoiceItemDetailView(APIView):
    def get(self, request, pk):
        invoice_item = get_object_or_404(InvoiceItem, pk=pk)
        serializer = InvoiceItemSerializer(invoice_item)
        return Response(serializer.data)

class InvoicePaymentDetailView(APIView):
    def get(self, request, pk):
        invoice_payment = get_object_or_404(InvoicePayment, pk=pk)
        serializer = InvoicePaymentSerializer(invoice_payment)
        return Response(serializer.data)

class SoldItemDetailView(APIView):
    def get(self, request, pk):
        sold_item = get_object_or_404(SoldItem, pk=pk)
        serializer = SoldItemSerializer(sold_item)
        return Response(serializer.data)

class ProvidedServiceDetailView(APIView):
    def get(self, request, pk):
        provided_service = get_object_or_404(ProvidedService, pk=pk)
        serializer = ProvidedServiceSerializer(provided_service)
        return Response(serializer.data)

class ProvidedServiceEnplDetailView(APIView):
    def get(self, request, pk):
        provided_service_enpl = get_object_or_404(ProvidedServiceEnpl, pk=pk)
        serializer = ProvidedServiceEnplSerializer(provided_service_enpl)
        return Response(serializer.data)
