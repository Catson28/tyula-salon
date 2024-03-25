from django.db import models
from apps.person.models import Person

# Create your models here.

class Employee(models.Model):
    position = models.CharField(max_length=255)  # Cargo do funcionário
    work_schedule = models.CharField(max_length=255)  # Horário de trabalho do funcionário
    person = models.OneToOneField(Person, on_delete=models.CASCADE)  # Referência à pessoa associada
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

#   Faltas
class Absence(models.Model):
    absence_date = models.DateField()  # Data de ausência
    reason = models.TextField()  # Motivo da ausência
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)  # Funcionário associado à ausência
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Salary(models.Model):
    payment_period = models.CharField(max_length=255)  # Período de pagamento
    base_salary = models.DecimalField(max_digits=10, decimal_places=2)  # Salário base
    deductions = models.DecimalField(max_digits=10, decimal_places=2)  # Deduções
    net_salary = models.DecimalField(max_digits=10, decimal_places=2)  # Salário líquido
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)  # Funcionário associado ao salário
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class EmployeePayment(models.Model):
    payment_date = models.DateField()  # Data do pagamento
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)  # Valor pago
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)  # Funcionário associado ao pagamento
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Representa um subsídio dado ao funcionário
class Subsidy(models.Model):
    subsidy_type = models.CharField(max_length=100)  # Tipo de subsídio (por exemplo, alimentação, transporte)
    subsidy_value = models.DecimalField(max_digits=10, decimal_places=2)  # Valor do subsídio
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Representa horas extras trabalhadas por um funcionário
class OvertimeHours(models.Model):
    hours_worked = models.DecimalField(max_digits=5, decimal_places=2)  # Horas trabalhadas
    overtime_hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)  # Taxa por hora extra
    total_overtime_hours = models.DecimalField(max_digits=5, decimal_places=2)  # Total de horas extras
    overtime_value = models.DecimalField(max_digits=10, decimal_places=2)  # Valor das horas extras
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Representa uma comissão recebida por um funcionário por vendas
class Commission(models.Model):
    sale_value = models.DecimalField(max_digits=10, decimal_places=2)  # Valor da venda
    commission_rate = models.DecimalField(max_digits=5, decimal_places=2)  # Taxa de comissão
    commission_value = models.DecimalField(max_digits=10, decimal_places=2)  # Valor da comissão
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Representa um bônus concedido a um funcionário
class Bonus(models.Model):
    bonus_type = models.CharField(max_length=100)  # Tipo de bônus (por exemplo, por desempenho, por tempo de serviço)
    bonus_value = models.DecimalField(max_digits=10, decimal_places=2)  # Valor do bônus
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Representa um adiantamento dado a um funcionário
class Advance(models.Model):
    advanced_value = models.DecimalField(max_digits=10, decimal_places=2)  # Valor do adiantamento
    advance_date = models.DateField()  # Data do adiantamento
    advance_details = models.TextField()  # Detalhes do adiantamento
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Representa um tipo de desconto aplicado ao salário
class Deduction(models.Model):
    deduction_type = models.CharField(max_length=100)  # Tipo de desconto (por exemplo, Segurança Social, IRS)
    deduction_value = models.DecimalField(max_digits=10, decimal_places=2)  # Valor do desconto
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
