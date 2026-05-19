from django.contrib import admin
from .models import Moto

@admin.register(Moto)
class MotoAdmin(admin.ModelAdmin):
    list_display = ['nom', 'immatriculation', 'type_moto', 'montant_journalier', 'etat']
    list_filter = ['etat', 'type_moto']
    search_fields = ['nom', 'immatriculation']
