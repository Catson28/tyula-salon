from django.db import models


# Modelo de pagamento
class Payment(models.Model):
    date = models.DateField()  # Data do pagamento
    paid = models.DecimalField(max_digits=10, decimal_places=2)  # Valor pago
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Representa um relatório de pagamento
class PaymentReport(models.Model):
    REPORT_TYPES = (
        ('monthly_summary', 'Monthly Summary'),  # Resumo mensal
        ('individual_payment_details', 'Individual Payment Details'),  # Detalhes de pagamento individual
        ('tax_statements', 'Tax Statements'),  # Declarações fiscais
        ('payment_history', 'Payment History'),  # Histórico de pagamentos
    )
    type = models.CharField(max_length=100, choices=REPORT_TYPES)  # Tipo de relatório
    # Adicione outros campos conforme necessário para tipos específicos de relatórios
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
