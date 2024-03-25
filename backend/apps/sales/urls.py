from django.urls import path
from . import views
from .views import (
    seller_list,
    invoice_category_list,
    invoice_list,
    invoice_item_list,
    invoice_payment_list,
    sold_item_list,
    provided_service_list,
    provided_service_enpl_list,
)

urlpatterns = [
    path('sellers/', seller_list, name='seller-list'),
    path('invoice-categories/', invoice_category_list, name='invoice-category-list'),
    path('invoices/', invoice_list, name='invoice-list'),
    path('invoice-items/', invoice_item_list, name='invoice-item-list'),
    path('invoice-payments/', invoice_payment_list, name='invoice-payment-list'),
    path('sold-items/', sold_item_list, name='sold-item-list'),
    path('provided-services/', provided_service_list, name='provided-service-list'),
    path('provided-service-enpl/', provided_service_enpl_list, name='provided-service-enpl-list'),
    path('add_seller/', views.create_seller, name='create_seller'),
    path('add_invoice_category/', views.create_invoice_category, name='create_invoice_category'),
    path('add_invoice/', views.create_invoice, name='create_invoice'),
    path('add_invoice_item/', views.create_invoice_item, name='create_invoice_item'),
    path('add_invoice_payment/', views.create_invoice_payment, name='create_invoice_payment'),
    path('add_sold_item/', views.create_sold_item, name='create_sold_item'),
    path('add_provided_service/', views.create_provided_service, name='create_provided_service'),
    path('add_provided_service_enpl/', views.create_provided_service_enpl, name='create_provided_service_enpl'),
    path('seller/<int:pk>/', views.SellerDetailView.as_view(), name='seller-detail'),
    path('invoice-category/<int:pk>/', views.InvoiceCategoryDetailView.as_view(), name='invoice-category-detail'),
    path('invoice/<int:pk>/', views.InvoiceDetailView.as_view(), name='invoice-detail'),
    path('invoice-item/<int:pk>/', views.InvoiceItemDetailView.as_view(), name='invoice-item-detail'),
    path('invoice-payment/<int:pk>/', views.InvoicePaymentDetailView.as_view(), name='invoice-payment-detail'),
    path('sold-item/<int:pk>/', views.SoldItemDetailView.as_view(), name='sold-item-detail'),
    path('provided-service/<int:pk>/', views.ProvidedServiceDetailView.as_view(), name='provided-service-detail'),
    path('provided-service-enpl/<int:pk>/', views.ProvidedServiceEnplDetailView.as_view(), name='provided-service-enpl-detail'),
]
