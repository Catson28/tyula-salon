from django.urls import path
from . import views

urlpatterns = [
    # Rotas relacionadas aos produtos
    path("add/", views.add_service),  # Adiciona um novo produto
    path("edit/<int:service_id>/", views.edit_service),  # Edita um produto existente
    path(
        "delete/<int:service_id>/", views.delete_service
    ),  # Deleta um produto existente
    path(
        "show/<int:service_id>/", views.show_service
    ),  # Mostra os detalhes de um produto
    path(
        "upload-image/", views.upload_service_image
    ),  # Faz o upload de imagens de um produto
    path(
        "delete-image/<int:image_id>/", views.delete_service_image
    ),  # Deleta uma imagem de produto
    path(
        "select-cover-image/<int:image_id>/", views.select_service_cover_image
    ),  # Seleciona a imagem de capa de um produto
    path(
        "select-or-upload-raw-material/", views.select_or_upload_raw_material
    ),  # Seleciona ou faz o upload de matéria-prima para um produto
    path(
        "select-or-upload-categories/", views.select_or_upload_categories
    ),  # Seleciona ou faz o upload de categorias ou subcategorias para um produto
]
