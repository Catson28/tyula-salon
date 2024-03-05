from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from apps.product.models import Product
from apps.material.models import RawMaterial



class Image(models.Model):
    ImageID = models.AutoField(primary_key=True)
    Path = models.CharField(max_length=255)
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={'model__in': ('product', 'materiaprima', 'cliente', 'profissional', 'user')}
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="prod_img")
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name="img_prod")

class RawMaterialImage(models.Model):
    raw_material = models.ForeignKey(RawMaterial, on_delete=models.CASCADE, related_name="raw_mat_img")
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name="img_raw_mat")
