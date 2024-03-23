from django.urls import path
from . import views

urlpatterns = [
    path("list/", views.list_services),  # Lista todos os serviços
    path("add/", views.create_service),  # Cria um novo serviço
    path("update/<int:service_id>/", views.update_service),  # Atualiza um serviço existente
    path("retrieve/<int:service_id>/", views.retrieve_service),  # Recupera os detalhes de um serviço
    path("delete/<int:service_id>/", views.delete_service),  # Deleta um serviço existente
    path("deleteAll/", views.delete_all_services),  # Deleta todos os serviços existentes
    path("upload-image/<int:service_id>/", views.upload_service_image),  # Faz o upload de imagens de um serviço
    path("delete-image/<int:image_id>/", views.delete_service_image),  # Deleta uma imagem de serviço
    path("select-cover-image/<int:service_id>/", views.select_service_cover_image),  # Seleciona a imagem de capa de um serviço
    path("select-or-upload-raw-material/<int:service_id>/", views.select_or_upload_raw_material),  # Seleciona ou faz o upload de matéria-prima para um serviço
    path("select-or-upload-categories/<int:service_id>/", views.select_or_upload_categories),  # Seleciona ou faz o upload de categorias ou subcategorias para um serviço
    path("list-products/<int:service_id>/", views.list_products),  # Lista todos os produtos relacionados a um serviço
    path("add-product/<int:service_id>/", views.add_product),  # Adiciona um novo produto relacionado a um serviço
    path("update-product/<int:product_id>/", views.update_product),  # Atualiza um produto relacionado a um serviço
    path("retrieve-product/<int:product_id>/", views.retrieve_product),  # Recupera os detalhes de um produto relacionado a um serviço
    path("delete-product/<int:product_id>/", views.delete_product),  # Deleta um produto relacionado a um serviço
]
