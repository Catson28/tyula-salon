from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Sale, ClientSale, ServiceSale
from .serializers import SaleSerializer, ClientSaleSerializer, ServiceSaleSerializer

@api_view(['POST'])
def create_sale(request):
    serializer = SaleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def select_or_register_professional(request):
    # Logic for selecting or registering a professional for a sale
    pass

@api_view(['POST'])
def select_or_register_customer(request):
    # Logic for selecting or registering a customer for a sale
    pass

@api_view(['POST'])
def select_payment_type(request):
    # Logic for selecting payment type for a sale
    pass

@api_view(['GET'])
def search_service(request):
    # Logic for searching services
    pass

@api_view(['GET'])
def list_service_with_cover(request):
    # Logic for listing services with cover images
    pass
