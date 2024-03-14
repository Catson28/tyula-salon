from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Professional
from .serializers import ProfessionalSerializer


@api_view(["POST"])
def create_professional(request):
    serializer = ProfessionalSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(["PUT"])
def edit_professional(request, professional_id):
    professional = get_object_or_404(Professional, pk=professional_id)
    serializer = ProfessionalSerializer(professional, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(["DELETE"])
def delete_professional(request, professional_id):
    professional = get_object_or_404(Professional, pk=professional_id)
    professional.delete()
    return Response(status=204)


@api_view(["GET"])
def show_professional(request, professional_id):
    professional = get_object_or_404(Professional, pk=professional_id)
    serializer = ProfessionalSerializer(professional)
    return Response(serializer.data)


@api_view(["GET"])
def list_professionals(request):
    professionals = Professional.objects.all()
    serializer = ProfessionalSerializer(professionals, many=True)
    return Response(serializer.data)
