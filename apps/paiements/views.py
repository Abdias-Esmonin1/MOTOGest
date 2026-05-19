from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.db.models import Sum
from .models import Paiement
from .forms import PaiementForm, SaisieJournaliereForm
from apps.motos.models import Moto
from datetime import datetime

@login_required
def saisie_journaliere(request):
    aujourd_hui = timezone.now().date()
    date_selectionnee = aujourd_hui

    if request.method == 'GET' and request.GET.get('date'):
        try:
            from datetime import date
            date_selectionnee = date.fromisoformat(request.GET.get('date'))
        except ValueError:
            pass

    motos = Moto.objects.filter(etat__in=['active', 'panne', 'maintenance'])
    paiements_existants = {p.moto_id: p for p in Paiement.objects.filter(date=date_selectionnee)}

    if request.method == 'POST':
        date_str = request.POST.get('date')
        from datetime import datetime
        try:
            date_saisie = datetime.strptime(date_str, "%Y-%m-%d").date() if date_str else aujourd_hui
        except ValueError:
            date_saisie = aujourd_hui

        for moto in motos:
            montant_verse = request.POST.get(f'montant_{moto.pk}', 0)
            statut = request.POST.get(f'statut_{moto.pk}', 'paye')
            obs = request.POST.get(f'obs_{moto.pk}', '')
            try:
                montant_verse = int(montant_verse)
            except (ValueError, TypeError):
                montant_verse = 0

            Paiement.objects.update_or_create(
                moto=moto, date=date_saisie,
                defaults={
                    'montant_attendu': moto.montant_journalier,
                    'montant_verse': montant_verse,
                    'statut': statut,
                    'observations': obs,
                }
            )
        messages.success(request, f"Paiements du {date_saisie.strftime('%d/%m/%Y')} enregistrés.")
        return redirect('saisie_journaliere')

    entrees = []
    total_attendu = 0
    total_verse = 0
    for moto in motos:
        p = paiements_existants.get(moto.pk)
        entrees.append({'moto': moto, 'paiement': p})
        total_attendu += moto.montant_journalier
        if p:
            total_verse += p.montant_verse

    context = {
        'entrees': entrees,
        'date_selectionnee': date_selectionnee,
        'total_attendu': total_attendu,
        'total_verse': total_verse,
        'manque': total_attendu - total_verse,
    }
    return render(request, 'paiements/saisie_journaliere.html', context)

@login_required
def historique_paiements(request):
    paiements = Paiement.objects.select_related('moto').order_by('-date')[:100]
    total = paiements.aggregate(t=Sum('montant_verse'))['t'] or 0
    return render(request, 'paiements/historique.html', {'paiements': paiements, 'total': total})
