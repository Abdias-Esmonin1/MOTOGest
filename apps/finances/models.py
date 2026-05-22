from django.db import models
from apps.core.models import BaseModel


class Depense(BaseModel):
    TYPE_CHOICES = [
        ('depense', 'Dépense'),
        ('emprunt_caisse', 'Emprunt caisse'),
        ('remboursement_emprunt', 'Remboursement emprunt'),
    ]
    CATEGORIE_CHOICES = [
        ('carburant', 'Carburant'),
        ('reparation', 'Réparation'),
        ('assurance', 'Assurance'),
        ('administratif', 'Administratif'),
        ('personnel', 'Personnel'),
        ('emprunt', 'Emprunt caisse'),
        ('remboursement', 'Remboursement emprunt'),
        ('autre', 'Autre'),
    ]
    STATUT_REMBOURSEMENT_CHOICES = [
        ('non_rembourse', 'Non remboursé'),
        ('partiel', 'Partiel'),
        ('rembourse', 'Remboursé'),
    ]

    date = models.DateField()
    type_operation = models.CharField(max_length=30, choices=TYPE_CHOICES, default='depense')
    categorie = models.CharField(max_length=30, choices=CATEGORIE_CHOICES)
    montant = models.DecimalField(max_digits=10, decimal_places=0)
    description = models.CharField(max_length=255)
    personne = models.CharField(max_length=120, blank=True)
    statut_remboursement = models.CharField(
        max_length=30,
        choices=STATUT_REMBOURSEMENT_CHOICES,
        blank=True,
        default='',
    )
    date_remboursement_prevue = models.DateField(null=True, blank=True)
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
