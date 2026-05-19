from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_conducteurs, name='liste_conducteurs'),
    path('<int:pk>/', views.detail_conducteur, name='detail_conducteur'),
    path('ajouter/', views.ajouter_conducteur, name='ajouter_conducteur'),
    path('<int:pk>/modifier/', views.modifier_conducteur, name='modifier_conducteur'),
    path('<int:pk>/supprimer/', views.supprimer_conducteur, name='supprimer_conducteur'),
]
