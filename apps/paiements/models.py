from django.db import models
from apps.core.models import BaseModel
from apps.motos.models import Moto

class Paiement(BaseModel):
    STATUT_CHOICES = [
        ('paye', 'Payé'),
        ('partiel', 'Partiel'),
        ('absent', 'Absent'),
        ('panne', 'En panne'),
    ]

    moto = models.ForeignKey(Moto, on_delete=models.CASCADE, related_name='paiements')
    date = models.DateField()
    montant_attendu = models.DecimalField(max_digits=10, decimal_places=0)
    montant_verse = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='paye')
    observations = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Paiement'
        ordering = ['-date']
        unique_together = ['moto', 'date']

    def __str__(self):
        return f"{self.moto} - {self.date} - {self.montant_verse} FCFA"

    def manque_a_gagner(self):
        return max(0, self.montant_attendu - self.montant_verse)

    def taux_recouvrement(self):
        if self.montant_attendu == 0:
            return 0
        return round((self.montant_verse / self.montant_attendu) * 100, 1)
