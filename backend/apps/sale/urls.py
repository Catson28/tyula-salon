from django.urls import path
from . import views

urlpatterns = [
    # Rotas relacionadas às vendas
    path("create/", views.create_sale),  # Cria uma nova venda
    path(
        "select-or-register-professional/", views.select_or_register_professional
    ),  # Seleciona ou registra um profissional para uma venda
    path(
        "select-or-register-customer/", views.select_or_register_customer
    ),  # Seleciona ou registra um cliente para uma venda
    path(
        "select-payment-type/", views.select_payment_type
    ),  # Seleciona o tipo de pagamento para uma venda
    path("search-service/", views.search_service),  # Procura por um produto
    path(
        "list-service-with-cover/", views.list_service_with_cover
    ),  # Lista os produtos com suas imagens de capa
]
