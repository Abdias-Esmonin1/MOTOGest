from django.db import models
from apps.core.models import BaseModel
from apps.motos.models import Moto

class MaintenancePreventive(BaseModel):
    TYPE_CHOICES = [
        ('vidange', 'Vidange'),
        ('pneus', 'Pneus'),
        ('freins', 'Freins'),
        ('moteur', 'Révision moteur'),
        ('assurance', 'Assurance'),
        ('visite', 'Visite technique'),
        ('autre', 'Autre'),
    ]
    STATUT_CHOICES = [('planifie','Planifié'),('fait','Fait'),('urgent','Urgent'),('en_retard','En retard')]

    moto = models.ForeignKey(Moto, on_delete=models.CASCADE, related_name='maintenances')
    type_maintenance = models.CharField(max_length=30, choices=TYPE_CHOICES)
    date_prevue = models.DateField()
    date_realisation = models.DateField(null=True, blank=True)
    cout = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='planifie')
    notes = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Maintenance préventive'
        ordering = ['date_prevue']

    def __str__(self):
        return f"{self.moto} - {self.get_type_maintenance_display()} ({self.date_prevue})"

    def save(self, *args, **kwargs):
        from django.utils import timezone
        if not self.date_realisation:
            delta = (self.date_prevue - timezone.now().date()).days
            if delta < 0:
                self.statut = 'en_retard'
            elif delta <= 7:
                self.statut = 'urgent'
        super().save(*args, **kwargs)
