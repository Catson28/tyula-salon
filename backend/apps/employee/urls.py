from django.urls import path
from . import views
from .views import (
    employee_list,
    absence_list,
    salary_list,
    employee_payment_list,
    subsidy_list,
    overtime_hours_list,
    commission_list,
    bonus_list,
    advance_list,
    deduction_list,
)

urlpatterns = [
    path('employees/', employee_list, name='employee-list'),
    path('absences/', absence_list, name='absence-list'),
    path('salaries/', salary_list, name='salary-list'),
    path('employee-payments/', employee_payment_list, name='employee-payment-list'),
    path('subsidies/', subsidy_list, name='subsidy-list'),
    path('overtime-hours/', overtime_hours_list, name='overtime-hours-list'),
    path('commissions/', commission_list, name='commission-list'),
    path('bonuses/', bonus_list, name='bonus-list'),
    path('advances/', advance_list, name='advance-list'),
    path('deductions/', deduction_list, name='deduction-list'),
    path('add_employee/', views.create_employee, name='create_employee'),
    path('add_absence/', views.create_absence, name='create_absence'),
    path('add_salary/', views.create_salary, name='create_salary'),
    path('add_employee_payment/', views.create_employee_payment, name='create_employee_payment'),
    path('add_subsidy/', views.create_subsidy, name='create_subsidy'),
    path('add_overtime_hours/', views.create_overtime_hours, name='create_overtime_hours'),
    path('add_commission/', views.create_commission, name='create_commission'),
    path('add_bonus/', views.create_bonus, name='create_bonus'),
    path('add_advance/', views.create_advance, name='create_advance'),
    path('add_deduction/', views.create_deduction, name='create_deduction'),
    path('employee/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee-detail'),
    path('absence/<int:pk>/', views.AbsenceDetailView.as_view(), name='absence-detail'),
    path('salary/<int:pk>/', views.SalaryDetailView.as_view(), name='salary-detail'),
    path('employee-payment/<int:pk>/', views.EmployeePaymentDetailView.as_view(), name='employee-payment-detail'),
    path('subsidy/<int:pk>/', views.SubsidyDetailView.as_view(), name='subsidy-detail'),
    path('overtime-hours/<int:pk>/', views.OvertimeHoursDetailView.as_view(), name='overtime-hours-detail'),
    path('commission/<int:pk>/', views.CommissionDetailView.as_view(), name='commission-detail'),
    path('bonus/<int:pk>/', views.BonusDetailView.as_view(), name='bonus-detail'),
    path('advance/<int:pk>/', views.AdvanceDetailView.as_view(), name='advance-detail'),
    path('deduction/<int:pk>/', views.DeductionDetailView.as_view(), name='deduction-detail'),
]
