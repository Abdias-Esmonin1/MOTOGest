from django.contrib import admin
from .models import MaintenancePreventive

@admin.register(MaintenancePreventive)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ['moto', 'type_maintenance', 'date_prevue', 'statut']
    list_filter = ['statut', 'type_maintenance']
