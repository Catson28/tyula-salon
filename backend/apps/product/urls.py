from django.urls import path
from . import views

urlpatterns = [
    # Rotas relacionadas aos materiais brutos
    path("list/", views.list_products),  # Lista todos os materiais brutos
    path("add/", views.add_product),  # Adiciona um novo material bruto
    path(
        "update/<int:product_id>/", views.update_product
    ),  # Atualiza um material bruto existente
    path(
        "read/<int:product_id>/", views.read_product
    ),  # Mostra os detalhes de um material bruto
    path(
        "delete/<int:product_id>/", views.delete_product
    ),  # Deleta um material bruto existente
    path(
        "upload-image/", views.upload_product_image
    ),  # Faz o upload de imagens de um material bruto
    path(
        "delete-image/<int:image_id>/", views.delete_product_image
    ),  # Deleta uma imagem de material bruto
    path(
        "upload-cover-image/", views.upload_product_cover_image
    ),  # Faz o upload da imagem de capa de um material bruto
]
