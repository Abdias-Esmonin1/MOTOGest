from django.contrib import admin
from .models import Conducteur

@admin.register(Conducteur)
class ConducteurAdmin(admin.ModelAdmin):
    list_display = ['nom_complet', 'telephone', 'moto', 'actif']
    list_filter = ['actif']
