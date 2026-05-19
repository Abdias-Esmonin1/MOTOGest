from django import forms
from .models import Depense, Epargne

class DepenseForm(forms.ModelForm):
    class Meta:
        model = Depense
        fields = ['date','categorie','montant','description','notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 2}),
        }

class EpargneForm(forms.ModelForm):
    class Meta:
        model = Epargne
        fields = ['date','montant','description','notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 2}),
        }
