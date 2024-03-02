from django.urls import path
from . import views

urlpatterns = [
    # Rotas relacionadas aos produtos
    path('add/', views.add_product),  # Adiciona um novo produto
    path('edit/<int:product_id>/', views.edit_product),  # Edita um produto existente
    path('delete/<int:product_id>/', views.delete_product),  # Deleta um produto existente
    path('show/<int:product_id>/', views.show_product),  # Mostra os detalhes de um produto
    path('upload-image/', views.upload_product_image),  # Faz o upload de imagens de um produto
    path('delete-image/<int:image_id>/', views.delete_product_image),  # Deleta uma imagem de produto
    path('select-cover-image/<int:image_id>/', views.select_product_cover_image),  # Seleciona a imagem de capa de um produto
    path('select-or-upload-raw-material/', views.select_or_upload_raw_material),  # Seleciona ou faz o upload de matéria-prima para um produto
    path('select-or-upload-categories/', views.select_or_upload_categories),  # Seleciona ou faz o upload de categorias ou subcategorias para um produto
]
