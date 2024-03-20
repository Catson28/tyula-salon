from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Service
from .serializers import ServiceSerializer


@api_view(["GET"])
def list_services(request):
    services = Service.objects.all()
    serializer = ServiceSerializer(services, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def create_service(request):
    serializer = ServiceSerializer(data=request.data)
    print(request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def update_service(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    serializer = ServiceSerializer(service, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def retrieve_service(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    serializer = ServiceSerializer(service)
    return Response(serializer.data)


@api_view(["DELETE"])
def delete_service(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    service.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["POST"])
def upload_service_image(request, service_id):
    # Logic for uploading service image
    pass


@api_view(["DELETE"])
def delete_service_image(request, image_id):
    # Logic for deleting service image
    pass


@api_view(["POST"])
def select_service_cover_image(request, service_id):
    # Logic for selecting service cover image
    pass


@api_view(["POST"])
def select_or_upload_raw_material(request, service_id):
    # Logic for selecting or uploading raw material for a service
    pass


@api_view(["POST"])
def select_or_upload_categories(request, service_id):
    # Logic for selecting or uploading categories or subcategories for a service
    pass

@api_view(["DELETE"])
def delete_all_services(request):
    Service.objects.all().delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
