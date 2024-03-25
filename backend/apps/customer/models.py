from django.db import models
from apps.person.models import Person

class Customer(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)  # Referência à pessoa associada
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
