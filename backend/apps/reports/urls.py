from django.urls import path
from . import views
from .views import (
    sales_report_list,
    billing_report_list,
    frequent_customers_report_list,
    inventory_report_list,
)

urlpatterns = [
    path('sales-reports/', sales_report_list, name='sales-report-list'),
    path('billing-reports/', billing_report_list, name='billing-report-list'),
    path('frequent-customers-reports/', frequent_customers_report_list, name='frequent-customers-report-list'),
    path('inventory-reports/', inventory_report_list, name='inventory-report-list'),
    path('add_sales_report/', views.create_sales_report, name='create_sales_report'),
    path('add_billing_report/', views.create_billing_report, name='create_billing_report'),
    path('add_frequent_customers_report/', views.create_frequent_customers_report, name='create_frequent_customers_report'),
    path('add_inventory_report/', views.create_inventory_report, name='create_inventory_report'),
    path('sales-report/<int:pk>/', views.SalesReportDetailView.as_view(), name='sales-report-detail'),
    path('billing-report/<int:pk>/', views.BillingReportDetailView.as_view(), name='billing-report-detail'),
    path('frequent-customers-report/<int:pk>/', views.FrequentCustomersReportDetailView.as_view(), name='frequent-customers-report-detail'),
    path('inventory-report/<int:pk>/', views.InventoryReportDetailView.as_view(), name='inventory-report-detail'),
]
