from django import forms
from .models import Conducteur

class ConducteurForm(forms.ModelForm):
    class Meta:
        model = Conducteur
        fields = ['nom','prenom','telephone','adresse','photo','moto','date_debut','actif','observations']
        widgets = {
            'date_debut': forms.DateInput(attrs={'type': 'date'}),
            'adresse': forms.Textarea(attrs={'rows': 2}),
            'observations': forms.Textarea(attrs={'rows': 3}),
        }
