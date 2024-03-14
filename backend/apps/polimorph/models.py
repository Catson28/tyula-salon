# models.py

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)

class Comentario(models.Model):
    conteudo = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    autor = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    content_object = GenericForeignKey('content_type', 'object_id')

class Foto(models.Model):
    url = models.URLField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    autor = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    content_object = GenericForeignKey('content_type', 'object_id')
