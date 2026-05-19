from django import forms
from .models import Paiement
from apps.motos.models import Moto

class PaiementForm(forms.ModelForm):
    class Meta:
        model = Paiement
        fields = ['moto', 'date', 'montant_attendu', 'montant_verse', 'statut', 'observations']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'observations': forms.Textarea(attrs={'rows': 2}),
        }

class SaisieJournaliereForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
