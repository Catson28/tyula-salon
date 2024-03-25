from django.urls import path
from . import views
from .views import (
    credit_list,
    debit_list,
    accounts_receivable_list,
    pending_invoice_details_list,
)

urlpatterns = [
    path('credits/', credit_list, name='credit-list'),
    path('debits/', debit_list, name='debit-list'),
    path('accounts-receivable/', accounts_receivable_list, name='accounts-receivable-list'),
    path('pending-invoice-details/', pending_invoice_details_list, name='pending-invoice-details-list'),
    path('add_credit/', views.create_credit, name='create_credit'),
    path('add_debit/', views.create_debit, name='create_debit'),
    path('add_accounts_receivable/', views.create_accounts_receivable, name='create_accounts_receivable'),
    path('add_pending_invoice_details/', views.create_pending_invoice_details, name='create_pending_invoice_details'),
    path('credit/<int:pk>/', views.CreditDetailView.as_view(), name='credit-detail'),
    path('debit/<int:pk>/', views.DebitDetailView.as_view(), name='debit-detail'),
    path('accounts-receivable/<int:pk>/', views.AccountsReceivableDetailView.as_view(), name='accounts-receivable-detail'),
    path('pending-invoice-details/<int:pk>/', views.PendingInvoiceDetailsDetailView.as_view(), name='pending-invoice-details-detail'),
]
