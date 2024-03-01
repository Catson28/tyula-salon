from django.db import models
from apps.category.models import Category

class RawMaterial(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category_material")
