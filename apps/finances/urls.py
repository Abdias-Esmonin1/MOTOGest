from django.urls import path
from . import views

urlpatterns = [
    path('', views.tableau_bord_finances, name='tableau_bord_finances'),
    path('depense/ajouter/', views.ajouter_depense, name='ajouter_depense'),
    path('epargne/ajouter/', views.ajouter_epargne, name='ajouter_epargne'),
    path('repartition/', views.repartition_revenus, name='repartition_revenus'),
]
