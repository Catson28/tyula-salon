from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Image(models.Model):
    ImageID = models.AutoField(primary_key=True)
    Path = models.ImageField(upload_to="images/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class CategoryImage(models.Model):
    category = models.ForeignKey(
        'category.Category',  # Corrigido para usar string para referenciar o modelo
        on_delete=models.CASCADE,
        related_name="prd_img"
    )
    image = models.ForeignKey(
        Image,
        on_delete=models.CASCADE,
        related_name="img_cat"
    )
    cover = models.BooleanField(default=False)  # Adicionando o campo cover como booleano
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ServiceImage(models.Model):
    service = models.ForeignKey(
        'service.Service',  # Corrigido para usar string para referenciar o modelo
        on_delete=models.CASCADE,
        related_name="srv_img"
    )
    image = models.ForeignKey(
        Image,
        on_delete=models.CASCADE,
        related_name="img_srv"
    )
    cover = models.BooleanField(default=False)  # Adicionando o campo cover como booleano
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ProductImage(models.Model):
    product = models.ForeignKey(
        'product.Product',  # Corrigido para usar string para referenciar o modelo
        on_delete=models.CASCADE,
        related_name="prod_img"
    )
    image = models.ForeignKey(
        Image,
        on_delete=models.CASCADE,
        related_name="img_prod"
    )
    cover = models.BooleanField(default=False)  # Adicionando o campo cover como booleano
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
