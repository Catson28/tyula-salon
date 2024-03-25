from rest_framework import serializers
from .models import Employee, Absence, Salary, EmployeePayment, Subsidy, OvertimeHours, Commission, Bonus, Advance, Deduction

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'position', 'work_schedule', 'person']  

class AbsenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Absence
        fields = ['id', 'absence_date', 'reason', 'employee']  

class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = ['id', 'payment_period', 'base_salary', 'deductions', 'net_salary', 'employee']  

class EmployeePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeePayment
        fields = ['id', 'payment_date', 'amount_paid', 'employee']  

class SubsidySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subsidy
        fields = ['id', 'subsidy_type', 'subsidy_value']  

class OvertimeHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = OvertimeHours
        fields = ['id', 'hours_worked', 'overtime_hourly_rate', 'total_overtime_hours', 'overtime_value']  

class CommissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commission
        fields = ['id', 'sale_value', 'commission_rate', 'commission_value']  

class BonusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bonus
        fields = ['id', 'bonus_type', 'bonus_value']  

class AdvanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advance
        fields = ['id', 'advanced_value', 'advance_date', 'advance_details']  

class DeductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deduction
        fields = ['id', 'deduction_type', 'deduction_value']  












