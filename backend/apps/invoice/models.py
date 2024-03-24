from django.db import models

# Modelo de categoria de fatura
class CategoriaFatura(models.Model):
    nome = models.CharField(max_length=255)  # Nome da categoria

    def __str__(self):
        return self.nome

# Modelo de fatura
class Fatura(models.Model):
    numero_fatura = models.CharField(max_length=255)  # Número da fatura
    categoria = models.ForeignKey(CategoriaFatura, on_delete=models.CASCADE)  # Categoria da fatura
    data_emissao = models.DateField()  # Data de emissão da fatura
    data_vencimento = models.DateField()  # Data de vencimento da fatura
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)  # Valor total da fatura

# Modelo de item de fatura
class ItemFatura(models.Model):
    fatura = models.ForeignKey(Fatura, related_name='itens', on_delete=models.CASCADE)  # Fatura associada ao item
    descricao = models.TextField()  # Descrição do item
    quantidade = models.IntegerField()  # Quantidade do item
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)  # Preço unitário do item
    total_linha = models.DecimalField(max_digits=10, decimal_places=2)  # Total da linha para o item

# Modelo de pagamento
class Pagamento(models.Model):
    fatura = models.ForeignKey(Fatura, related_name='pagamentos', on_delete=models.CASCADE)  # Fatura associada ao pagamento
    data_pagamento = models.DateField()  # Data do pagamento
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2)  # Valor pago
