from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import MaintenancePreventive
from .forms import MaintenanceForm

@login_required
def liste_maintenances(request):
    maintenances = MaintenancePreventive.objects.select_related('moto').all()
    urgentes = maintenances.filter(statut__in=['urgent','en_retard'])
    return render(request, 'maintenance/liste.html', {'maintenances': maintenances, 'urgentes': urgentes})

@login_required
def ajouter_maintenance(request):
    form = MaintenanceForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Maintenance planifiée.")
        return redirect('liste_maintenances')
    return render(request, 'maintenance/formulaire.html', {'form': form, 'titre': 'Planifier une maintenance'})

@login_required
def modifier_maintenance(request, pk):
    m = get_object_or_404(MaintenancePreventive, pk=pk)
    form = MaintenanceForm(request.POST or None, instance=m)
    if form.is_valid():
        form.save()
        messages.success(request, "Maintenance mise à jour.")
        return redirect('liste_maintenances')
    return render(request, 'maintenance/formulaire.html', {'form': form, 'titre': 'Modifier', 'm': m})
