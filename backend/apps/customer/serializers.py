from rest_framework import serializers
from .models import Customer
from apps.person.serializers import PersonSerializer

class CustomerSerializer(serializers.ModelSerializer):
    person = PersonSerializer(read_only=True)
    class Meta:
        model = Customer
        fields = ["id", "person"]
