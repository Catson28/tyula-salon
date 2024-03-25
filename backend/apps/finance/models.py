from django.db import models
from apps.sales.models import Seller, Invoice
from apps.customer.models import Customer

# Créditos de Vendas
class Credit(models.Model):
    Credit_Reason = models.CharField(max_length=255)  # Motivo do Crédito
    Credit_Amount = models.DecimalField(max_digits=10, decimal_places=2)  # Valor do Crédito
    Credit_Date = models.DateField()  # Data do Crédito
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)  # ID do Vendedor (Chave Estrangeira)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  # ID do Cliente (Chave Estrangeira)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.Credit_Date} - {self.customer}"

# Débitos de Vendas
class Debit(models.Model):
    Debit_Reason = models.CharField(max_length=255)  # Motivo do Débito
    Debit_Amount = models.DecimalField(max_digits=10, decimal_places=2)  # Valor do Débito
    Debit_Date = models.DateField()  # Data do Débito
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)  # ID do Vendedor (Chave Estrangeira)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  # ID do Cliente (Chave Estrangeira)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.Debit_Date} - {self.customer}"

# Contas a Receber
class AccountsReceivable(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  # ID do Cliente (Chave Estrangeira)
    Total_Amount_Pending = models.DecimalField(max_digits=10, decimal_places=2)  # Valor Total Pendente
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer} - {self.Total_Amount_Pending}"

# Detalhes de Faturas Pendentes
class PendingInvoiceDetails(models.Model):
    Due_Date = models.DateField()  # Data de Vencimento
    Invoice_Amount = models.DecimalField(max_digits=10, decimal_places=2)  # Valor da Fatura
    Receivable_Account_ID = models.ForeignKey(AccountsReceivable, on_delete=models.CASCADE)  # ID da Conta a Receber (Chave Estrangeira)
    Invoice_ID = models.ForeignKey(Invoice, on_delete=models.CASCADE)  # ID da Fatura (Chave Estrangeira)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.Receivable_Account_ID} - {self.Invoice_Amount}"
