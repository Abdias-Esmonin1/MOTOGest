from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_pannes, name='liste_pannes'),
    path('ajouter/', views.ajouter_panne, name='ajouter_panne'),
    path('<int:pk>/', views.detail_panne, name='detail_panne'),
    path('<int:pk>/modifier/', views.modifier_panne, name='modifier_panne'),
]
