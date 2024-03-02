from django.urls import path
from . import views

urlpatterns = [
    # Rotas relacionadas aos materiais brutos
    path('list/', views.list_raw_materials),  # Lista todos os materiais brutos
    path('add/', views.add_raw_material),  # Adiciona um novo material bruto
    path('update/<int:raw_material_id>/', views.update_raw_material),  # Atualiza um material bruto existente
    path('read/<int:raw_material_id>/', views.read_raw_material),  # Mostra os detalhes de um material bruto
    path('delete/<int:raw_material_id>/', views.delete_raw_material),  # Deleta um material bruto existente
    path('upload-image/', views.upload_raw_material_image),  # Faz o upload de imagens de um material bruto
    path('delete-image/<int:image_id>/', views.delete_raw_material_image),  # Deleta uma imagem de material bruto
    path('upload-cover-image/', views.upload_raw_material_cover_image),  # Faz o upload da imagem de capa de um material bruto
]
