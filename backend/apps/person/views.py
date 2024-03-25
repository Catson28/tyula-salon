from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from rest_framework.views import APIView
from .serializers import PersonSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def person_list(request):
    people = Person.objects.all()
    serializer = PersonSerializer(people, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_person(request):
    serializer = PersonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonDetailView(APIView):
    def get(self, request, pk):
        person = get_object_or_404(Person, pk=pk)
        serializer = PersonSerializer(person)
        return Response(serializer.data)
