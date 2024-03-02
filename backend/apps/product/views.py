from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

@api_view(['POST'])
def add_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    serializer = ProductSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    return Response(status=204)

@api_view(['GET'])
def show_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

@api_view(['POST'])
def upload_product_image(request):
    # Logic for uploading product image
    pass

@api_view(['DELETE'])
def delete_product_image(request, image_id):
    # Logic for deleting product image
    pass

@api_view(['POST'])
def select_product_cover_image(request):
    # Logic for selecting product cover image
    pass

@api_view(['POST'])
def select_or_upload_raw_material(request):
    # Logic for selecting or uploading raw material for a product
    pass

@api_view(['POST'])
def select_or_upload_categories(request):
    # Logic for selecting or uploading categories or subcategories for a product
    pass
