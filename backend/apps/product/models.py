from django.db import models
from apps.category.models import Category
from apps.material.models import RawMaterial
from apps.subcategory.models import Subcategory

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    raw_material = models.ForeignKey(RawMaterial, on_delete=models.CASCADE, related_name="mat_prod")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="cat_prod")
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name="subcat_prod")
