from django.db import models

# Create your models here.
class Seller(models.Model):  # Define um modelo para representar um vendedor.
    seller_name = models.CharField(max_length=100)  # Define um campo para o nome do vendedor.