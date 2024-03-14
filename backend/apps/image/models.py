from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from apps.service.models import Service
from apps.product.models import Product


class Image(models.Model):
    ImageID = models.AutoField(primary_key=True)
    Path = models.ImageField(upload_to="images/")
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        # limit_choices_to={'model__in': ('service', 'materiaprima', 'cliente', 'profissional', 'user')}
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")


class ServiceImage(models.Model):
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name="prd_img"
    )
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name="img_prd")


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="prod_img"
    )
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name="img_prod")
