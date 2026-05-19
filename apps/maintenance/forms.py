from django import forms
from .models import MaintenancePreventive

class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = MaintenancePreventive
        fields = ['moto','type_maintenance','date_prevue','cout','statut','date_realisation','notes']
        widgets = {
            'date_prevue': forms.DateInput(attrs={'type': 'date'}),
            'date_realisation': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }
