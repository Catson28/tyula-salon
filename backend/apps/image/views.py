from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Image, ServiceImage, Product
from .serializers import ImageSerializer, ServiceImageSerializer, ProductSerializer

@api_view(['POST'])
def add_image(request):
    serializer = ImageSerializer(data=request.data)
    print(request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def view_image(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    serializer = ImageSerializer(image)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_image(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    image.delete()
    return Response(status=204)

@api_view(['POST'])
def associate_image_with_service(request):
    serializer = ServiceImageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def associate_image_with_raw_material(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def list_images_by_type(request):
    images = Image.objects.all()
    serializer = ImageSerializer(images, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def update_image_description(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    serializer = ImageSerializer(image, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)
