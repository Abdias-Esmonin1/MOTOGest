from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Moto
from .forms import MotoForm

@login_required
def liste_motos(request):
    motos = Moto.objects.all()
    return render(request, 'motos/liste.html', {'motos': motos})

@login_required
def detail_moto(request, pk):
    moto = get_object_or_404(Moto, pk=pk)
    paiements = moto.paiements.order_by('-date')[:30]
    pannes = moto.pannes.order_by('-date_panne')[:10]
    return render(request, 'motos/detail.html', {'moto': moto, 'paiements': paiements, 'pannes': pannes})

@login_required
def ajouter_moto(request):
    form = MotoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Moto ajoutée avec succès.")
        return redirect('liste_motos')
    return render(request, 'motos/formulaire.html', {'form': form, 'titre': 'Ajouter une moto'})

@login_required
def modifier_moto(request, pk):
    moto = get_object_or_404(Moto, pk=pk)
    form = MotoForm(request.POST or None, request.FILES or None, instance=moto)
    if form.is_valid():
        form.save()
        messages.success(request, "Moto modifiée avec succès.")
        return redirect('liste_motos')
    return render(request, 'motos/formulaire.html', {'form': form, 'titre': 'Modifier la moto', 'moto': moto})

@login_required
def supprimer_moto(request, pk):
    moto = get_object_or_404(Moto, pk=pk)
    if request.method == 'POST':
        moto.delete()
        messages.success(request, "Moto supprimée.")
        return redirect('liste_motos')
    return render(request, 'motos/confirmer_suppression.html', {'moto': moto})
