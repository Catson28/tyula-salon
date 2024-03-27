from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Subcategory
from .serializers import SubcategorySerializer, SubcategoryCreateSerializer


@api_view(["GET"])
def list_subcategories(request):
    subcategories = Subcategory.objects.all()
    serializer = SubcategorySerializer(subcategories, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def add_subcategory(request):
    print(request.data)
    serializer = SubcategoryCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(["PUT"])
def update_subcategory(request, subcategory_id):
    subcategory = get_object_or_404(Subcategory, pk=subcategory_id)
    serializer = SubcategorySerializer(subcategory, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(["GET"])
def read_subcategory(request, subcategory_id):
    subcategory = get_object_or_404(Subcategory, pk=subcategory_id)
    serializer = SubcategorySerializer(subcategory)
    return Response(serializer.data)


@api_view(["DELETE"])
def delete_subcategory(request, subcategory_id):
    subcategory = get_object_or_404(Subcategory, pk=subcategory_id)
    subcategory.delete()
    return Response(status=204)


@api_view(["DELETE"])
def delete_subcategories(request):
    Subcategory.objects.all().delete()
    return Response(status=204)


@api_view(["GET"])
def search_subcategory_by_name(request):
    name = request.GET.get("name", "")
    subcategories = Subcategory.objects.filter(name__icontains=name)
    serializer = SubcategorySerializer(subcategories, many=True)
    return Response(serializer.data)
