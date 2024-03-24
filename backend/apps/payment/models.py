from django.db import models

# Create your models here.


# Modelo de pagamento
class Payment(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='payments', on_delete=models.CASCADE)  # Fatura associada ao pagamento
    payment_date = models.DateField()  # Data do pagamento
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)  # Valor pago


class Payment(models.Model):
    payment_date = models.DateField()  # Data do pagamento
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)  # Funcionário associado ao pagamento
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)  # Valor pago

    
# Representa um relatório de pagamento
class PaymentReport(models.Model):
    REPORT_TYPES = (
        ('monthly_summary', 'Monthly Summary'),  # Resumo mensal
        ('individual_payment_details', 'Individual Payment Details'),  # Detalhes de pagamento individual
        ('tax_statements', 'Tax Statements'),  # Declarações fiscais
        ('payment_history', 'Payment History'),  # Histórico de pagamentos
    )
    report_type = models.CharField(max_length=100, choices=REPORT_TYPES)  # Tipo de relatório
    # Adicione outros campos conforme necessário para tipos específicos de relatórios