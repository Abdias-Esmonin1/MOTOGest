from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import FileResponse
from django.conf import settings
from django.utils import timezone
from django.views.decorators.cache import never_cache
from django.views.decorators.http import require_GET
from django.db.models import Sum
from datetime import timedelta

@login_required
def dashboard(request):
    from apps.motos.models import Moto
    from apps.paiements.models import Paiement
    from apps.pannes.models import Panne
    from apps.finances.models import Depense

    aujourd_hui = timezone.now().date()
    debut_mois = aujourd_hui.replace(day=1)
    debut_semaine = aujourd_hui - timedelta(days=aujourd_hui.weekday())

    motos_total = Moto.objects.count()
    motos_actives = Moto.objects.filter(etat='active').count()
    motos_panne = Moto.objects.filter(etat='panne').count()

    recettes_jour = Paiement.objects.filter(date=aujourd_hui).aggregate(t=Sum('montant_verse'))['t'] or 0
    recettes_semaine = Paiement.objects.filter(date__gte=debut_semaine).aggregate(t=Sum('montant_verse'))['t'] or 0
    recettes_mois = Paiement.objects.filter(date__gte=debut_mois).aggregate(t=Sum('montant_verse'))['t'] or 0

    depenses_mois = Depense.objects.filter(date__gte=debut_mois).aggregate(t=Sum('montant'))['t'] or 0
    benefice_mois = recettes_mois - depenses_mois

    paiements_recents = Paiement.objects.select_related('moto').order_by('-date', '-created_at')[:10]
    pannes_recentes = Panne.objects.select_related('moto').order_by('-date_panne')[:5]

    # Données graphiques 6 derniers mois
    labels_mois = []
    data_recettes = []
    data_depenses = []
    for i in range(5, -1, -1):
        d = aujourd_hui - timedelta(days=30 * i)
        debut = d.replace(day=1)
        if debut.month == 12:
            fin = debut.replace(year=debut.year + 1, month=1, day=1)
        else:
            fin = debut.replace(month=debut.month + 1, day=1)
        r = Paiement.objects.filter(date__gte=debut, date__lt=fin).aggregate(t=Sum('montant_verse'))['t'] or 0
        dep = Depense.objects.filter(date__gte=debut, date__lt=fin).aggregate(t=Sum('montant'))['t'] or 0
        labels_mois.append(debut.strftime('%b %Y'))
        data_recettes.append(float(r))
        data_depenses.append(float(dep))

    context = {
        'motos_total': motos_total,
        'motos_actives': motos_actives,
        'motos_panne': motos_panne,
        'recettes_jour': recettes_jour,
        'recettes_semaine': recettes_semaine,
        'recettes_mois': recettes_mois,
        'depenses_mois': depenses_mois,
        'benefice_mois': benefice_mois,
        'paiements_recents': paiements_recents,
        'pannes_recentes': pannes_recentes,
        'labels_mois': labels_mois,
        'data_recettes': data_recettes,
        'data_depenses': data_depenses,
        'aujourd_hui': aujourd_hui,
    }
    return render(request, 'core/dashboard.html', context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    erreur = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            erreur = "Identifiants incorrects."
    return render(request, 'login.html', {'erreur': erreur})

def logout_view(request):
    logout(request)
    return redirect('login')

@require_GET
@never_cache
def service_worker(request):
    response = FileResponse(
        open(settings.BASE_DIR / 'static' / 'service-worker.js', 'rb'),
        content_type='application/javascript',
    )
    response['Service-Worker-Allowed'] = '/'
    return response

@require_GET
def manifest(request):
    return FileResponse(
        open(settings.BASE_DIR / 'static' / 'manifest.webmanifest', 'rb'),
        content_type='application/manifest+json',
    )

def offline(request):
    return render(request, 'offline.html')
