from django.utils import timezone
from apps.pannes.models import Panne
from apps.maintenance.models import MaintenancePreventive

def global_context(request):
    if not request.user.is_authenticated:
        return {}
    pannes_actives = Panne.objects.filter(statut='en_cours').count()
    maintenances_urgentes = MaintenancePreventive.objects.filter(
        statut='urgent'
    ).count()
    return {
        'pannes_actives': pannes_actives,
        'maintenances_urgentes': maintenances_urgentes,
        'aujourd_hui': timezone.now().date(),
    }
