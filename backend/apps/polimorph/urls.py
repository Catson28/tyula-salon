# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.FuncionarioCreate.as_view(), name='comentario-list-create'),
    path('comentarios/', views.ComentarioListCreate.as_view(), name='comentario-list-create'),
    path('fotos/', views.FotoListCreate.as_view(), name='foto-list-create'),
]
