from django.urls import path
from ..category import views

urlpatterns = [
    # Rotas relacionadas às categorias
    path('list/', views.list_categories),  # Lista todas as categorias
    path('add/', views.add_category),  # Adiciona uma nova categoria
    path('update/<int:category_id>/', views.update_category),  # Atualiza uma categoria existente
    path('read/<int:category_id>/', views.read_category),  # Mostra os detalhes de uma categoria
    path('delete/<int:category_id>/', views.delete_category),  # Deleta uma categoria existente
    path('deleteAll/', views.delete_categories),  # Deleta uma categoria existente
    path('search', views.search_category_by_name),  # Busca categoria por nome
]
