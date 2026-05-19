from django.contrib import admin
from .models import Paiement

@admin.register(Paiement)
class PaiementAdmin(admin.ModelAdmin):
    list_display = ['date', 'moto', 'montant_verse', 'montant_attendu', 'statut']
    list_filter = ['statut', 'date']
    date_hierarchy = 'date'
