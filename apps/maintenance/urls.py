from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_maintenances, name='liste_maintenances'),
    path('ajouter/', views.ajouter_maintenance, name='ajouter_maintenance'),
    path('<int:pk>/modifier/', views.modifier_maintenance, name='modifier_maintenance'),
]
