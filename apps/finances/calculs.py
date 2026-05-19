from django.utils import timezone
from django.db.models import Sum
from datetime import timedelta

def get_stats_financieres(periode='mois'):
    from apps.paiements.models import Paiement
    from apps.finances.models import Depense

    aujourd_hui = timezone.now().date()

    if periode == 'jour':
        debut = aujourd_hui
    elif periode == 'semaine':
        debut = aujourd_hui - timedelta(days=aujourd_hui.weekday())
    elif periode == 'mois':
        debut = aujourd_hui.replace(day=1)
    elif periode == 'annee':
        debut = aujourd_hui.replace(month=1, day=1)
    else:
        debut = aujourd_hui.replace(day=1)

    recettes = Paiement.objects.filter(date__gte=debut).aggregate(t=Sum('montant_verse'))['t'] or 0
    depenses = Depense.objects.filter(date__gte=debut).aggregate(t=Sum('montant'))['t'] or 0
    benefice = recettes - depenses

    return {
        'recettes': recettes,
        'depenses': depenses,
        'benefice': benefice,
        'repartition': {
            'epargne': round(float(recettes) * 0.35),
            'maintenance': round(float(recettes) * 0.25),
            'reinvestissement': round(float(recettes) * 0.20),
            'personnel': round(float(recettes) * 0.20),
        }
    }
