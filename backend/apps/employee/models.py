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

class Payment(models.Model):
    payment_date = models.DateField()  # Data do pagamento
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)  # Funcionário associado ao pagamento
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)  # Valor pago
