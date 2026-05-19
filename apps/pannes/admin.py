from django.contrib import admin
from .models import Panne

@admin.register(Panne)
class PanneAdmin(admin.ModelAdmin):
    list_display = ['moto', 'type_panne', 'date_panne', 'cout_reparation', 'statut']
    list_filter = ['statut']
