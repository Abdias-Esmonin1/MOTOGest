from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_motos, name='liste_motos'),
    path('<int:pk>/', views.detail_moto, name='detail_moto'),
    path('ajouter/', views.ajouter_moto, name='ajouter_moto'),
    path('<int:pk>/modifier/', views.modifier_moto, name='modifier_moto'),
    path('<int:pk>/supprimer/', views.supprimer_moto, name='supprimer_moto'),
]
