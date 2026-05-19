from django.contrib import admin
from .models import Depense, Epargne

@admin.register(Depense)
class DepenseAdmin(admin.ModelAdmin):
    list_display = ['date', 'categorie', 'description', 'montant']
    list_filter = ['categorie']
    date_hierarchy = 'date'

@admin.register(Epargne)
class EpargneAdmin(admin.ModelAdmin):
    list_display = ['date', 'montant', 'description']
