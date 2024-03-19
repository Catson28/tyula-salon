from django.db import models
from apps.image.models import CategoryImage


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    path = None
