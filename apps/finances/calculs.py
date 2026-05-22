from django.utils import timezone
from django.db.models import Sum
from datetime import timedelta


def get_debut_periode(periode='mois'):
    aujourd_hui = timezone.now().date()

    if periode == 'jour':
        return aujourd_hui
    if periode == 'semaine':
        return aujourd_hui - timedelta(days=aujourd_hui.weekday())
    if periode == 'annee':
        return aujourd_hui.replace(month=1, day=1)
    return aujourd_hui.replace(day=1)


def somme_depenses(queryset):
    return queryset.aggregate(t=Sum('montant'))['t'] or 0


def get_stats_financieres(periode='mois'):
    from apps.paiements.models import Paiement
    from apps.finances.models import Depense

    debut = get_debut_periode(periode)

    recettes = Paiement.objects.filter(date__gte=debut).aggregate(t=Sum('montant_verse'))['t'] or 0
    mouvements = Depense.objects.filter(date__gte=debut)

    depenses_reelles = somme_depenses(mouvements.filter(type_operation='depense'))
    emprunts_caisse = somme_depenses(mouvements.filter(type_operation='emprunt_caisse'))
    remboursements_emprunts = somme_depenses(mouvements.filter(type_operation='remboursement_emprunt'))

    sorties_caisse = depenses_reelles + emprunts_caisse
    entrees_caisse = recettes + remboursements_emprunts
    benefice = recettes - depenses_reelles
    solde_caisse = entrees_caisse - sorties_caisse

    return {
        'recettes': recettes,
        'depenses': depenses_reelles,
        'emprunts_caisse': emprunts_caisse,
        'remboursements_emprunts': remboursements_emprunts,
        'sorties_caisse': sorties_caisse,
        'entrees_caisse': entrees_caisse,
        'benefice': benefice,
        'solde_caisse': solde_caisse,
        'repartition': {
            'epargne': round(float(recettes) * 0.35),
            'maintenance': round(float(recettes) * 0.25),
            'reinvestissement': round(float(recettes) * 0.20),
            'personnel': round(float(recettes) * 0.20),
        }
    }
