from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Service
from .serializers import ServiceSerializer


@api_view(["POST"])
def add_service(request):
    serializer = ServiceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(["PUT"])
def edit_service(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    serializer = ServiceSerializer(service, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(["DELETE"])
def delete_service(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    service.delete()
    return Response(status=204)


@api_view(["GET"])
def show_service(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    serializer = ServiceSerializer(service)
    return Response(serializer.data)


@api_view(["POST"])
def upload_service_image(request):
    # Logic for uploading service image
    pass


@api_view(["DELETE"])
def delete_service_image(request, image_id):
    # Logic for deleting service image
    pass


@api_view(["POST"])
def select_service_cover_image(request):
    # Logic for selecting service cover image
    pass


@api_view(["POST"])
def select_or_upload_raw_material(request):
    # Logic for selecting or uploading raw material for a service
    pass


@api_view(["POST"])
def select_or_upload_categories(request):
    # Logic for selecting or uploading categories or subcategories for a service
    pass
