from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from .models import Panne
from .forms import PanneForm

@login_required
def liste_pannes(request):
    pannes = Panne.objects.select_related('moto').all()
    total_cout = pannes.aggregate(t=Sum('cout_reparation'))['t'] or 0
    return render(request, 'pannes/liste.html', {'pannes': pannes, 'total_cout': total_cout})

@login_required
def ajouter_panne(request):
    form = PanneForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        panne = form.save()
        if panne.statut == 'en_cours':
            panne.moto.etat = 'panne'
            panne.moto.save()
        messages.success(request, "Panne enregistrée.")
        return redirect('liste_pannes')
    return render(request, 'pannes/formulaire.html', {'form': form, 'titre': 'Déclarer une panne'})

@login_required
def modifier_panne(request, pk):
    panne = get_object_or_404(Panne, pk=pk)
    form = PanneForm(request.POST or None, request.FILES or None, instance=panne)
    if form.is_valid():
        p = form.save()
        if p.statut == 'reparee':
            p.moto.etat = 'active'
            p.moto.save()
        messages.success(request, "Panne mise à jour.")
        return redirect('liste_pannes')
    return render(request, 'pannes/formulaire.html', {'form': form, 'titre': 'Modifier la panne', 'panne': panne})

@login_required
def detail_panne(request, pk):
    panne = get_object_or_404(Panne, pk=pk)
    return render(request, 'pannes/detail.html', {'panne': panne})
