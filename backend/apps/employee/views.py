from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import EmployeeSerializer, AbsenceSerializer, SalarySerializer, EmployeePaymentSerializer, SubsidySerializer, OvertimeHoursSerializer, CommissionSerializer, BonusSerializer, AdvanceSerializer, DeductionSerializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from .models import Employee, Absence, Salary, EmployeePayment, Subsidy, OvertimeHours, Commission, Bonus, Advance, Deduction
from .serializers import (
    EmployeeSerializer,
    AbsenceSerializer,
    SalarySerializer,
    EmployeePaymentSerializer,
    SubsidySerializer,
    OvertimeHoursSerializer,
    CommissionSerializer,
    BonusSerializer,
    AdvanceSerializer,
    DeductionSerializer,
)

@api_view(['GET'])
def employee_list(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def absence_list(request):
    absences = Absence.objects.all()
    serializer = AbsenceSerializer(absences, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def salary_list(request):
    salaries = Salary.objects.all()
    serializer = SalarySerializer(salaries, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def employee_payment_list(request):
    employee_payments = EmployeePayment.objects.all()
    serializer = EmployeePaymentSerializer(employee_payments, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def subsidy_list(request):
    subsidies = Subsidy.objects.all()
    serializer = SubsidySerializer(subsidies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def overtime_hours_list(request):
    overtime_hours = OvertimeHours.objects.all()
    serializer = OvertimeHoursSerializer(overtime_hours, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def commission_list(request):
    commissions = Commission.objects.all()
    serializer = CommissionSerializer(commissions, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def bonus_list(request):
    bonuses = Bonus.objects.all()
    serializer = BonusSerializer(bonuses, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def advance_list(request):
    advances = Advance.objects.all()
    serializer = AdvanceSerializer(advances, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def deduction_list(request):
    deductions = Deduction.objects.all()
    serializer = DeductionSerializer(deductions, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def create_employee(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_absence(request):
    serializer = AbsenceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_salary(request):
    serializer = SalarySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_employee_payment(request):
    serializer = EmployeePaymentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_subsidy(request):
    serializer = SubsidySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_overtime_hours(request):
    serializer = OvertimeHoursSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_commission(request):
    serializer = CommissionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_bonus(request):
    serializer = BonusSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_advance(request):
    serializer = AdvanceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_deduction(request):
    serializer = DeductionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeDetailView(APIView):
    def get(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

class AbsenceDetailView(APIView):
    def get(self, request, pk):
        absence = get_object_or_404(Absence, pk=pk)
        serializer = AbsenceSerializer(absence)
        return Response(serializer.data)

class SalaryDetailView(APIView):
    def get(self, request, pk):
        salary = get_object_or_404(Salary, pk=pk)
        serializer = SalarySerializer(salary)
        return Response(serializer.data)

class EmployeePaymentDetailView(APIView):
    def get(self, request, pk):
        employee_payment = get_object_or_404(EmployeePayment, pk=pk)
        serializer = EmployeePaymentSerializer(employee_payment)
        return Response(serializer.data)

class SubsidyDetailView(APIView):
    def get(self, request, pk):
        subsidy = get_object_or_404(Subsidy, pk=pk)
        serializer = SubsidySerializer(subsidy)
        return Response(serializer.data)

class OvertimeHoursDetailView(APIView):
    def get(self, request, pk):
        overtime_hours = get_object_or_404(OvertimeHours, pk=pk)
        serializer = OvertimeHoursSerializer(overtime_hours)
        return Response(serializer.data)

class CommissionDetailView(APIView):
    def get(self, request, pk):
        commission = get_object_or_404(Commission, pk=pk)
        serializer = CommissionSerializer(commission)
        return Response(serializer.data)

class BonusDetailView(APIView):
    def get(self, request, pk):
        bonus = get_object_or_404(Bonus, pk=pk)
        serializer = BonusSerializer(bonus)
        return Response(serializer.data)

class AdvanceDetailView(APIView):
    def get(self, request, pk):
        advance = get_object_or_404(Advance, pk=pk)
        serializer = AdvanceSerializer(advance)
        return Response(serializer.data)

class DeductionDetailView(APIView):
    def get(self, request, pk):
        deduction = get_object_or_404(Deduction, pk=pk)
        serializer = DeductionSerializer(deduction)
        return Response(serializer.data)
