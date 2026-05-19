from django import forms
from .models import Moto

class MotoForm(forms.ModelForm):
    class Meta:
        model = Moto
        fields = ['nom','immatriculation','type_moto','montant_journalier','etat','date_achat','photo','observations']
        widgets = {
            'date_achat': forms.DateInput(attrs={'type': 'date'}),
            'observations': forms.Textarea(attrs={'rows': 3}),
        }
