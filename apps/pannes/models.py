from django.db import models
from apps.core.models import BaseModel
from apps.motos.models import Moto

class Panne(BaseModel):
    STATUT_CHOICES = [('en_cours','En cours'),('reparee','Réparée'),('abandonnee','Abandonnée')]

    moto = models.ForeignKey(Moto, on_delete=models.CASCADE, related_name='pannes')
    date_panne = models.DateField()
    date_reparation = models.DateField(null=True, blank=True)
    type_panne = models.CharField(max_length=100)
    description = models.TextField()
    cout_reparation = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    garagiste = models.CharField(max_length=100, blank=True)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_cours')
    facture = models.ImageField(upload_to='pannes/', null=True, blank=True)
    observations = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Panne'
        ordering = ['-date_panne']

    def __str__(self):
        return f"{self.moto} - {self.type_panne} ({self.date_panne})"

    def duree_immobilisation(self):
        if self.date_reparation:
            return (self.date_reparation - self.date_panne).days
        from django.utils import timezone
        return (timezone.now().date() - self.date_panne).days
