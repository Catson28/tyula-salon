from django.db import models

# Create your models here.
# Tabela para armazenar informações comuns a todas as entidades (funcionários, professores, clientes, visitantes)
class Person(models.Model):
    # Chave primária que identifica cada pessoa de forma única
    name = models.CharField(max_length=255)  # Nome da pessoa
    address = models.CharField(max_length=255)  # Endereço da pessoa
    contact = models.CharField(max_length=255)  # Informações de contato da pessoa
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'People'