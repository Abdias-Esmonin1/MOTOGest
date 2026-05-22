from django.contrib import admin
from .models import Depense, Epargne

@admin.register(Depense)
class DepenseAdmin(admin.ModelAdmin):
    list_display = ['date', 'type_operation', 'categorie', 'description', 'personne', 'montant', 'statut_remboursement']
    list_filter = ['type_operation', 'categorie', 'statut_remboursement']
    search_fields = ['description', 'personne', 'notes']
    date_hierarchy = 'date'

@admin.register(Epargne)
class EpargneAdmin(admin.ModelAdmin):
    list_display = ['date', 'montant', 'description']
