from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=255)  # Nome do funcionário
    position = models.CharField(max_length=255)  # Cargo do funcionário
    work_schedule = models.CharField(max_length=255)  # Horário de trabalho do funcionário

    def __str__(self):
        return self.name

class Absence(models.Model):
    absence_date = models.DateField()  # Data de ausência
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)  # Funcionário associado à ausência
    reason = models.TextField()  # Motivo da ausência

class Salary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)  # Funcionário associado ao salário
    payment_period = models.CharField(max_length=255)  # Período de pagamento
    base_salary = models.DecimalField(max_digits=10, decimal_places=2)  # Salário base
    deductions = models.DecimalField(max_digits=10, decimal_places=2)  # Deduções
    net_salary = models.DecimalField(max_digits=10, decimal_places=2)  # Salário líquido

class EmployeePayment(models.Model):
    payment_date = models.DateField()  # Data do pagamento
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)  # Funcionário associado ao pagamento
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)  # Valor pago

# Representa um subsídio dado ao funcionário
class Subsidy(models.Model):
    subsidy_type = models.CharField(max_length=100)  # Tipo de subsídio (por exemplo, alimentação, transporte)
    subsidy_value = models.DecimalField(max_digits=10, decimal_places=2)  # Valor do subsídio

# Representa horas extras trabalhadas por um funcionário
class OvertimeHours(models.Model):
    hours_worked = models.DecimalField(max_digits=5, decimal_places=2)  # Horas trabalhadas
    overtime_hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)  # Taxa por hora extra
    total_overtime_hours = models.DecimalField(max_digits=5, decimal_places=2)  # Total de horas extras
    overtime_value = models.DecimalField(max_digits=10, decimal_places=2)  # Valor das horas extras

# Representa uma comissão recebida por um funcionário por vendas
class Commission(models.Model):
    sale_value = models.DecimalField(max_digits=10, decimal_places=2)  # Valor da venda
    commission_rate = models.DecimalField(max_digits=5, decimal_places=2)  # Taxa de comissão
    commission_value = models.DecimalField(max_digits=10, decimal_places=2)  # Valor da comissão

# Representa um bônus concedido a um funcionário
class Bonus(models.Model):
    bonus_type = models.CharField(max_length=100)  # Tipo de bônus (por exemplo, por desempenho, por tempo de serviço)
    bonus_value = models.DecimalField(max_digits=10, decimal_places=2)  # Valor do bônus

# Representa um adiantamento dado a um funcionário
class Advance(models.Model):
    advanced_value = models.DecimalField(max_digits=10, decimal_places=2)  # Valor do adiantamento
    advance_date = models.DateField()  # Data do adiantamento
    advance_details = models.TextField()  # Detalhes do adiantamento
