from django.urls import path
from ..subcategory import views

urlpatterns = [
    # Rotas relacionadas às subcategorias
    path("list/", views.list_subcategories),  # Lista todas as subcategorias
    path("add/", views.add_subcategory),  # Adiciona uma nova subcategoria
    path(
        "update/<int:subcategory_id>/", views.update_subcategory
    ),  # Atualiza uma subcategoria existente
    path(
        "read/<int:subcategory_id>/", views.read_subcategory
    ),  # Mostra os detalhes de uma subcategoria
    path(
        "delete/<int:subcategory_id>/", views.delete_subcategory
    ),  # Deleta uma subcategoria existente
    path("deleteAll/", views.delete_subcategories),  # Deleta uma subcategoria existente
    path("search", views.search_subcategory_by_name),  # Busca subcategoria por nome
]
