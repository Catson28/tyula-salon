from django.db import models
from apps.person.models import Person
from apps.customer.models import Customer
from apps.product.models import Product
from apps.service.models import Service
from apps.employee.models import Employee

# Create your models here.
class Seller(models.Model):  # Define um modelo para representar um vendedor.
    type = models.CharField(max_length=100)  # Define um campo para o nome do vendedor.
    person = models.OneToOneField(Person, on_delete=models.CASCADE)  # Referência à pessoa associada
    

# Modelo de categoria de fatura
class InvoiceCategory(models.Model):
    name = models.CharField(max_length=255)  # Nome da categoria

    def __str__(self):
        return self.name
    
# Modelo de fatura
class Invoice(models.Model):
    invoice_number = models.CharField(max_length=255)  # Número da fatura
    issuance_date = models.DateField()  # Data de emissão da fatura
    due_date = models.DateField()  # Data de vencimento da fatura
    payment_type = models.CharField(max_length=100)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Valor total da fatura
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)  # Define uma relação com o vendedor da fatura.
    client = models.ForeignKey(Customer, on_delete=models.CASCADE)  # Define uma relação com o cliente da fatura.
    category = models.ForeignKey(InvoiceCategory, on_delete=models.CASCADE)  # Categoria da fatura


# Modelo de item de fatura
class InvoiceItem(models.Model):
    description = models.TextField()  # Descrição do item
    quantity = models.IntegerField()  # Quantidade do item
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)  # Preço unitário do item
    line_total = models.DecimalField(max_digits=10, decimal_places=2)  # Total da linha para o item
    invoice = models.ForeignKey(Invoice, related_name='items', on_delete=models.CASCADE)  # Fatura associada ao item

# Modelo de pagamento
class InvoicePayment(models.Model):
    payment_date = models.DateField()  # Data do pagamento
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)  # Valor pago
    invoice = models.ForeignKey(Invoice, related_name='payments', on_delete=models.CASCADE)  # Fatura associada ao pagamento

# Define um modelo para representar um item vendido.
class SoldItem(models.Model):  
    quantity = models.IntegerField()  # Define um campo para a quantidade do produto vendido.
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)  # Define uma relação com a fatura do item.
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Define uma relação com o produto vendido.

# Define um modelo para representar um serviço prestado.
class ProvidedService(models.Model):  
    service_date_duration = models.CharField(max_length=100)  # Define um campo para a duração do serviço.
    alternative_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_service_value = models.DecimalField(max_digits=10, decimal_places=2)  # Define um campo para o valor total do serviço.
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)  # Define uma relação com a fatura do serviço.
    service = models.ForeignKey(Service, on_delete=models.CASCADE)  # Define uma relação com o serviço prestado.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Define um modelo para representar um serviço prestado pelo trabalhador.
class ProvidedServiceEnpl(models.Model):  
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="profess_sale"
    )
    provided_service = models.ForeignKey(
        ProvidedService, on_delete=models.CASCADE, related_name="sale_clisal"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

