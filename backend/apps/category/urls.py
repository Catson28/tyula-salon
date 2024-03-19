from django.urls import path, include
from ..category import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'(?P<category_id>\d+)/list/img', views.CategoryImageViewSet, basename='category-images')

urlpatterns = [

    path('', include(router.urls)),
    # Rotas relacionadas às categorias
    path("list/", views.list_categories),  # Lista todas as categorias
    path("add/", views.add_category),  # Adiciona uma nova categoria
    path(
        "update/<int:category_id>/", views.update_category
    ),  # Atualiza uma categoria existente
    path(
        "read/<int:category_id>/", views.read_category
    ),  # Mostra os detalhes de uma categoria
    path(
        "delete/<int:category_id>/", views.delete_category
    ),  # Deleta uma categoria existente
    path("deleteAll/", views.delete_categories),  # Deleta uma categoria existente
    path("search", views.search_category_by_name),  # Busca categoria por nome
]
