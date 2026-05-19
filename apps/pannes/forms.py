from django import forms
from .models import Panne

class PanneForm(forms.ModelForm):
    class Meta:
        model = Panne
        fields = ['moto','date_panne','type_panne','description','cout_reparation','garagiste','statut','date_reparation','facture','observations']
        widgets = {
            'date_panne': forms.DateInput(attrs={'type': 'date'}),
            'date_reparation': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
            'observations': forms.Textarea(attrs={'rows': 2}),
        }
