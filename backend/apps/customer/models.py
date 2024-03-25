from django.db import models
from apps.employee.models import Employee

class Customer(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)  # Referência à pessoa associada
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
