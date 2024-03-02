from django.urls import path
from . import views

urlpatterns = [
    # Rotas relacionadas aos profissionais
    path('create/', views.create_professional),  # Cria um novo profissional
    path('edit/<int:professional_id>/', views.edit_professional),  # Edita um profissional existente
    path('delete/<int:professional_id>/', views.delete_professional),  # Deleta um profissional existente
    path('show/<int:professional_id>/', views.show_professional),  # Mostra os detalhes de um profissional
    path('list/', views.list_professionals),  # Lista todos os profissionais
]
