from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Conducteur
from .forms import ConducteurForm

@login_required
def liste_conducteurs(request):
    conducteurs = Conducteur.objects.select_related('moto').all()
    return render(request, 'conducteurs/liste.html', {'conducteurs': conducteurs})

@login_required
def detail_conducteur(request, pk):
    conducteur = get_object_or_404(Conducteur, pk=pk)
    return render(request, 'conducteurs/detail.html', {'conducteur': conducteur})

@login_required
def ajouter_conducteur(request):
    form = ConducteurForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Conducteur ajouté avec succès.")
        return redirect('liste_conducteurs')
    return render(request, 'conducteurs/formulaire.html', {'form': form, 'titre': 'Ajouter un conducteur'})

@login_required
def modifier_conducteur(request, pk):
    conducteur = get_object_or_404(Conducteur, pk=pk)
    form = ConducteurForm(request.POST or None, request.FILES or None, instance=conducteur)
    if form.is_valid():
        form.save()
        messages.success(request, "Conducteur modifié.")
        return redirect('liste_conducteurs')
    return render(request, 'conducteurs/formulaire.html', {'form': form, 'titre': 'Modifier le conducteur'})

@login_required
def supprimer_conducteur(request, pk):
    conducteur = get_object_or_404(Conducteur, pk=pk)
    if request.method == 'POST':
        conducteur.delete()
        messages.success(request, "Conducteur supprimé.")
        return redirect('liste_conducteurs')
    return render(request, 'conducteurs/confirmer_suppression.html', {'conducteur': conducteur})
