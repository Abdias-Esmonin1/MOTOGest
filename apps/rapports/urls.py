from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_rapports, name='index_rapports'),
    path('excel/', views.rapport_excel, name='rapport_excel'),
    path('pdf/', views.rapport_pdf, name='rapport_pdf'),
]
