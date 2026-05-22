from django import forms
from .models import Depense, Epargne

class DepenseForm(forms.ModelForm):
    class Meta:
        model = Depense
        fields = [
            'date',
            'type_operation',
            'categorie',
            'montant',
            'description',
            'personne',
            'statut_remboursement',
            'date_remboursement_prevue',
            'notes',
        ]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'date_remboursement_prevue': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 2}),
        }

    def clean(self):
        cleaned_data = super().clean()
        type_operation = cleaned_data.get('type_operation')
        personne = cleaned_data.get('personne')

        if type_operation in ['emprunt_caisse', 'remboursement_emprunt'] and not personne:
            self.add_error('personne', "Indiquez la personne concernée par ce mouvement.")

        if type_operation == 'emprunt_caisse' and not cleaned_data.get('statut_remboursement'):
            cleaned_data['statut_remboursement'] = 'non_rembourse'

        if type_operation != 'emprunt_caisse':
            cleaned_data['date_remboursement_prevue'] = None
            if type_operation == 'remboursement_emprunt':
                cleaned_data['statut_remboursement'] = 'rembourse'
            else:
                cleaned_data['statut_remboursement'] = ''

        return cleaned_data

class EpargneForm(forms.ModelForm):
    class Meta:
        model = Epargne
        fields = ['date','montant','description','notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 2}),
        }
