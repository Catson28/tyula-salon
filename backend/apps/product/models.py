from django.db import models
from apps.category.models import Category


class Product(models.Model):
    name = models.CharField(max_length=100)
    cost = models.CharField(max_length=100) #   Preco da compra do produto
    description = models.TextField()
    quantity = models.FloatField(max_length=100) # quantidade de produtos em estoque
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="category_material"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
