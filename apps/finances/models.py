from django.db import models
from apps.core.models import BaseModel

class Depense(BaseModel):
    CATEGORIE_CHOICES = [
        ('carburant','Carburant'),('reparation','Réparation'),
        ('assurance','Assurance'),('administratif','Administratif'),
        ('personnel','Personnel'),('autre','Autre'),
    ]
    date = models.DateField()
    categorie = models.CharField(max_length=30, choices=CATEGORIE_CHOICES)
    montant = models.DecimalField(max_digits=10, decimal_places=0)
    description = models.CharField(max_length=255)
    notes = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Dépense'
        ordering = ['-date']

    def __str__(self):
        return f"{self.description} - {self.montant} FCFA ({self.date})"

class Epargne(BaseModel):
    date = models.DateField()
    montant = models.DecimalField(max_digits=10, decimal_places=0)
    description = models.CharField(max_length=255, blank=True)
    notes = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Épargne'
        ordering = ['-date']

    def __str__(self):
        return f"Épargne {self.date} - {self.montant} FCFA"
