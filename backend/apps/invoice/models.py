from django.db import models  # Importa o módulo de modelos do Django.

# Modelo de categoria de fatura
class InvoiceCategory(models.Model):
    name = models.CharField(max_length=255)  # Nome da categoria

    def __str__(self):
        return self.name

# Modelo de fatura
class Invoice(models.Model):
    invoice_number = models.CharField(max_length=255)  # Número da fatura
    category = models.ForeignKey(InvoiceCategory, on_delete=models.CASCADE)  # Categoria da fatura
    issuance_date = models.DateField()  # Data de emissão da fatura
    due_date = models.DateField()  # Data de vencimento da fatura
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Valor total da fatura

# Modelo de item de fatura
class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='items', on_delete=models.CASCADE)  # Fatura associada ao item
    description = models.TextField()  # Descrição do item
    quantity = models.IntegerField()  # Quantidade do item
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)  # Preço unitário do item
    line_total = models.DecimalField(max_digits=10, decimal_places=2)  # Total da linha para o item

# Modelo de pagamento
class Payment(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='payments', on_delete=models.CASCADE)  # Fatura associada ao pagamento
    payment_date = models.DateField()  # Data do pagamento
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)  # Valor pago
