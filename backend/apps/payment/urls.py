from django.urls import path
from . import views
from .views import payment_list, payment_report_list

urlpatterns = [
    path('payments/', payment_list, name='payment-list'),
    path('payment-reports/', payment_report_list, name='payment-report-list'),
    path('add_payment/', views.create_payment, name='create_payment'),
    path('add_payment_report/', views.create_payment_report, name='create_payment_report'),
    path('payment/<int:pk>/', views.PaymentDetailView.as_view(), name='payment-detail'),
    path('payment-report/<int:pk>/', views.PaymentReportDetailView.as_view(), name='payment-report-detail'),
]
