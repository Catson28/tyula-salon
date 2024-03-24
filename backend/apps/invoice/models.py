from django.db import models  # Importa o módulo de modelos do Django.

# Modelo de categoria de fatura
class InvoiceCategory(models.Model):
    name = models.CharField(max_length=255)  # Nome da categoria

    def __str__(self):
        return self.name

# Modelo de fatura
class Invoice(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)  # Define uma relação com o vendedor da fatura.
    client = models.ForeignKey(Client, on_delete=models.CASCADE)  # Define uma relação com o cliente da fatura.
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
class InvoicePayment(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='payments', on_delete=models.CASCADE)  # Fatura associada ao pagamento
    payment_date = models.DateField()  # Data do pagamento
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)  # Valor pago


class SoldItem(models.Model):  # Define um modelo para representar um item vendido.
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)  # Define uma relação com a fatura do item.
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Define uma relação com o produto vendido.
    quantity = models.IntegerField()  # Define um campo para a quantidade do produto vendido.

class ProvidedService(models.Model):  # Define um modelo para representar um serviço prestado.
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)  # Define uma relação com a fatura do serviço.
    service = models.ForeignKey(Service, on_delete=models.CASCADE)  # Define uma relação com o serviço prestado.
    service_date_duration = models.CharField(max_length=100)  # Define um campo para a duração do serviço.
    total_service_value = models.DecimalField(max_digits=10, decimal_places=2)  # Define um campo para o valor total do serviço.

# criar tabela de relacionamento de muitos para muitos de ProvidedService com trabalhadores