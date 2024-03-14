from django.urls import path
from . import views

urlpatterns = [
    # Rotas relacionadas aos clientes
    path("add/", views.add_customer),  # Adiciona um novo cliente
    path("edit/<int:customer_id>/", views.edit_customer),  # Edita um cliente existente
    path(
        "delete/<int:customer_id>/", views.delete_customer
    ),  # Deleta um cliente existente
    path(
        "show/<int:customer_id>/", views.show_customer
    ),  # Mostra os detalhes de um cliente
    path("list/", views.list_customers),  # Lista todos os clientes
    path("search/", views.search_customer),  # Procura por um cliente
    path(
        "associate-with-sale/", views.associate_customer_with_sale
    ),  # Associa um cliente a uma venda
]
