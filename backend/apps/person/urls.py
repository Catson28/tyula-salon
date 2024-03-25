from django.urls import path
from . import views
from .views import person_list

urlpatterns = [
    path('people/', person_list, name='person-list'),
    path('add_person/', views.create_person, name='create_person'),
    path('person/<int:pk>/', views.PersonDetailView.as_view(), name='person-detail'),
]
