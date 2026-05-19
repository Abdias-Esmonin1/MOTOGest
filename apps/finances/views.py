from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from .models import Depense, Epargne
from .forms import DepenseForm, EpargneForm
from .calculs import get_stats_financieres

PERIODE_CHOICES = {
    'jour': 'Aujourd\'hui',
    'semaine': 'Cette semaine',
    'mois': 'Ce mois',
    'annee': 'Cette année',
}

@login_required
def tableau_bord_finances(request):
    periode = request.GET.get('periode', 'mois')
    if periode not in PERIODE_CHOICES:
        periode = 'mois'
    stats = get_stats_financieres(periode)
    depenses_recentes = Depense.objects.order_by('-date')[:20]
    return render(request, 'finances/tableau_bord.html', {
        'stats': stats,
        'depenses_recentes': depenses_recentes,
        'periode': periode,
        'periode_choices': PERIODE_CHOICES,
    })

@login_required
def ajouter_depense(request):
    form = DepenseForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Dépense enregistrée.")
        return redirect('tableau_bord_finances')
    return render(request, 'finances/formulaire_depense.html', {'form': form})

@login_required
def ajouter_epargne(request):
    form = EpargneForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Épargne enregistrée.")
        return redirect('tableau_bord_finances')
    return render(request, 'finances/formulaire_epargne.html', {'form': form})

@login_required
def repartition_revenus(request):
    stats = get_stats_financieres('mois')
    return render(request, 'finances/repartition.html', {'stats': stats})
