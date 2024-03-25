from django.db import models  # Importa o módulo de modelos do Django.
from apps.person.models import Person
from apps.product.models import Product
from apps.service.models import Service
from apps.customer.models import Customer

# Relatórios de Vendas
class SalesReport(models.Model):
    Sale_Date = models.DateField()  # Data da Venda
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  # ID do Cliente (Chave Estrangeira)
    Total_Sale = models.DecimalField(max_digits=10, decimal_places=2)  # Total da Venda
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.Sale_Date} - {self.customer}"

# Relatórios de Faturamento
class BillingReport(models.Model):
    Period = models.CharField(max_length=255)  # Período
    Total_Invoices_Issued = models.IntegerField()  # Total de Faturas Emitidas
    Total_Invoices_Paid = models.IntegerField()  # Total de Faturas Pagas
    Total_Invoices_Pending = models.IntegerField()  # Total de Faturas Pendentes
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Period

# Relatórios de Clientes Frequentes
class FrequentCustomersReport(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  # ID do Cliente (Chave Estrangeira)
    Num_Purchases = models.IntegerField()  # Número de Compras
    Total_Purchase_Value = models.DecimalField(max_digits=10, decimal_places=2)  # Valor Total das Compras
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer} - {self.Num_Purchases}"

# Relatórios de Inventário
class InventoryReport(models.Model):
    Available_Products = models.IntegerField()  # Produtos Disponíveis
    Quantity_Sold = models.IntegerField()  # Quantidade Vendida
    Replenishment_Quantity = models.IntegerField()  # Quantidade de Reposição
    Low_Stock_Alerts = models.BooleanField(default=False)  # Alertas de Estoque Baixo
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.Available_Products} - {self.Quantity_Sold}"
