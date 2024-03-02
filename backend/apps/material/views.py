from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import RawMaterial
from .serializers import RawMaterialSerializer

@api_view(['GET'])
def list_raw_materials(request):
    raw_materials = RawMaterial.objects.all()
    serializer = RawMaterialSerializer(raw_materials, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_raw_material(request):
    serializer = RawMaterialSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def update_raw_material(request, raw_material_id):
    raw_material = get_object_or_404(RawMaterial, pk=raw_material_id)
    serializer = RawMaterialSerializer(raw_material, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def read_raw_material(request, raw_material_id):
    raw_material = get_object_or_404(RawMaterial, pk=raw_material_id)
    serializer = RawMaterialSerializer(raw_material)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_raw_material(request, raw_material_id):
    raw_material = get_object_or_404(RawMaterial, pk=raw_material_id)
    raw_material.delete()
    return Response(status=204)

@api_view(['POST'])
def upload_raw_material_image(request):
    # Logic for uploading raw material image
    pass

@api_view(['DELETE'])
def delete_raw_material_image(request, image_id):
    # Logic for deleting raw material image
    pass

@api_view(['POST'])
def upload_raw_material_cover_image(request):
    # Logic for uploading raw material cover image
    pass
