from django.db import models
from apps.core.models import BaseModel
from apps.motos.models import Moto

class Conducteur(BaseModel):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    adresse = models.TextField(blank=True)
    photo = models.ImageField(upload_to='conducteurs/', null=True, blank=True)
    moto = models.ForeignKey(Moto, on_delete=models.SET_NULL, null=True, blank=True, related_name='conducteurs')
    date_debut = models.DateField()
    actif = models.BooleanField(default=True)
    observations = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Conducteur'
        ordering = ['nom', 'prenom']

    def __str__(self):
        return f"{self.prenom} {self.nom}"

    def nom_complet(self):
        return f"{self.prenom} {self.nom}"
