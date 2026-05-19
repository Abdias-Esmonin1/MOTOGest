from django.urls import path
from . import views

urlpatterns = [
    path('', views.saisie_journaliere, name='saisie_journaliere'),
    path('historique/', views.historique_paiements, name='historique_paiements'),
]
