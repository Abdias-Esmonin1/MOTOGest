from django.db import models
from apps.core.models import BaseModel

class Moto(BaseModel):
    TYPE_CHOICES = [('taxi', 'Moto Taxi'), ('ordures', 'Ramassage Ordures')]
    ETAT_CHOICES = [('active','Active'),('panne','En panne'),('maintenance','Maintenance'),('repos','Repos')]

    nom = models.CharField(max_length=100)
    immatriculation = models.CharField(max_length=50, unique=True)
    type_moto = models.CharField(max_length=20, choices=TYPE_CHOICES, default='taxi')
    montant_journalier = models.DecimalField(max_digits=10, decimal_places=0, default=8000)
    etat = models.CharField(max_length=20, choices=ETAT_CHOICES, default='active')
    date_achat = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to='motos/', null=True, blank=True)
    observations = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Moto'
        ordering = ['nom']

    def __str__(self):
        return f"{self.nom} ({self.immatriculation})"

    def conducteur_actuel(self):
        return self.conducteurs.filter(actif=True).first()
