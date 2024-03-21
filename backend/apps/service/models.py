from django.db import models
from apps.category.models import Category
from apps.product.models import Product
from apps.subcategory.models import Subcategory
from apps.image.models import ServiceImage


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="cat_prod"
        )
    subcategory = models.ForeignKey(
        Subcategory, on_delete=models.CASCADE, related_name="subcat_prod")
    products = models.ManyToManyField(Product, through='ServiceProduct', related_name='services')

class ServiceProduct(models.Model):
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE)
    utilizacao = models.CharField(max_length=100)  # Adicione outros campos conforme necessário
