"""
Script de configuration initiale — MotoGest
Crée : admin, motos, conducteurs, paiements, pannes, maintenances, dépenses
Usage : python setup_demo.py
"""
import os, sys, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date, timedelta
import random

from apps.motos.models import Moto
from apps.conducteurs.models import Conducteur
from apps.paiements.models import Paiement
from apps.pannes.models import Panne
from apps.maintenance.models import MaintenancePreventive
from apps.finances.models import Depense, Epargne

print("🚀 Initialisation MotoGest...")

# ── ADMIN ──────────────────────────────────────────────
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@motogest.ci', 'admin123')
    print("✅ Admin créé — login: admin / mdp: admin123")
else:
    print("ℹ️  Admin déjà existant")

# ── MOTOS ──────────────────────────────────────────────
motos_data = [
    {'nom': 'Moto Taxi Alpha', 'immatriculation': 'CI-5421-TX', 'type_moto': 'taxi',    'montant_journalier': 8000, 'etat': 'active',  'date_achat': date(2022, 3, 15)},
    {'nom': 'Moto Taxi Bravo', 'immatriculation': 'CI-7832-TX', 'type_moto': 'taxi',    'montant_journalier': 8000, 'etat': 'active',  'date_achat': date(2022, 8, 20)},
    {'nom': 'Moto Ordures',    'immatriculation': 'CI-1104-OR', 'type_moto': 'ordures', 'montant_journalier': 5000, 'etat': 'active',  'date_achat': date(2023, 1, 10)},
]
motos = []
for d in motos_data:
    m, created = Moto.objects.get_or_create(immatriculation=d['immatriculation'], defaults=d)
    motos.append(m)
    if created: print(f"  🏍️  Moto créée : {m.nom}")

# ── CONDUCTEURS ────────────────────────────────────────
conducteurs_data = [
    {'nom': 'Kouassi', 'prenom': 'Koffi',    'telephone': '07 11 22 33', 'moto': motos[0], 'date_debut': date(2022, 4, 1)},
    {'nom': 'Bamba',   'prenom': 'Seydou',   'telephone': '05 44 55 66', 'moto': motos[1], 'date_debut': date(2022, 9, 1)},
    {'nom': 'Traoré',  'prenom': 'Ibrahim',  'telephone': '01 77 88 99', 'moto': motos[2], 'date_debut': date(2023, 2, 1)},
]
for d in conducteurs_data:
    c, created = Conducteur.objects.get_or_create(
        nom=d['nom'], prenom=d['prenom'],
        defaults={**d, 'actif': True}
    )
    if created: print(f"  👤 Conducteur créé : {c.nom_complet()}")

# ── PAIEMENTS (90 derniers jours) ──────────────────────
aujourd_hui = date.today()
STATUTS = ['paye', 'paye', 'paye', 'paye', 'partiel', 'absent', 'panne']

paiements_crees = 0
for i in range(89, -1, -1):
    jour = aujourd_hui - timedelta(days=i)
    # Pas de paiement le dimanche
    if jour.weekday() == 6:
        continue
    for moto in motos:
        if Paiement.objects.filter(moto=moto, date=jour).exists():
            continue
        statut = random.choices(STATUTS, weights=[60,60,60,60,15,8,5])[0]
        if statut == 'paye':
            verse = int(moto.montant_journalier)
        elif statut == 'partiel':
            verse = int(moto.montant_journalier) // 2
        else:
            verse = 0
        Paiement.objects.create(
            moto=moto, date=jour,
            montant_attendu=moto.montant_journalier,
            montant_verse=verse, statut=statut
        )
        paiements_crees += 1
print(f"  💰 {paiements_crees} paiements générés")

# ── PANNES ─────────────────────────────────────────────
pannes_data = [
    {'moto': motos[0], 'date_panne': aujourd_hui - timedelta(days=45), 'date_reparation': aujourd_hui - timedelta(days=42), 'type_panne': 'Crevaison pneu avant', 'description': 'Pneu avant crevé sur la route de Cocody', 'cout_reparation': 5000, 'garagiste': 'Garage Yao', 'statut': 'reparee'},
    {'moto': motos[1], 'date_panne': aujourd_hui - timedelta(days=20), 'date_reparation': aujourd_hui - timedelta(days=17), 'type_panne': 'Problème frein arrière', 'description': 'Câble de frein arrière cassé', 'cout_reparation': 8500, 'garagiste': 'Garage Central', 'statut': 'reparee'},
    {'moto': motos[2], 'date_panne': aujourd_hui - timedelta(days=5),  'date_reparation': None, 'type_panne': 'Moteur en surchauffe', 'description': 'Moteur chauffe anormalement, fuite huile détectée', 'cout_reparation': 0, 'garagiste': 'Garage Yao', 'statut': 'en_cours'},
]
for d in pannes_data:
    p, created = Panne.objects.get_or_create(
        moto=d['moto'], date_panne=d['date_panne'], type_panne=d['type_panne'],
        defaults=d
    )
    if created: print(f"  🔧 Panne créée : {p.type_panne} ({p.moto.nom})")

# Mettre moto ordures en panne si panne en cours
motos[2].etat = 'panne'
motos[2].save()

# ── MAINTENANCES ───────────────────────────────────────
maintenances_data = [
    {'moto': motos[0], 'type_maintenance': 'vidange', 'date_prevue': aujourd_hui + timedelta(days=3),  'cout': 3500, 'statut': 'urgent'},
    {'moto': motos[1], 'type_maintenance': 'pneus',   'date_prevue': aujourd_hui + timedelta(days=14), 'cout': 12000,'statut': 'planifie'},
    {'moto': motos[2], 'type_maintenance': 'assurance','date_prevue': aujourd_hui + timedelta(days=30),'cout': 45000,'statut': 'planifie'},
    {'moto': motos[0], 'type_maintenance': 'visite',  'date_prevue': aujourd_hui - timedelta(days=2),  'cout': 5000, 'statut': 'en_retard'},
]
for d in maintenances_data:
    m, created = MaintenancePreventive.objects.get_or_create(
        moto=d['moto'], type_maintenance=d['type_maintenance'], date_prevue=d['date_prevue'],
        defaults=d
    )
    if created: print(f"  🔩 Maintenance planifiée : {m.get_type_maintenance_display()} — {m.moto.nom}")

# ── DÉPENSES ───────────────────────────────────────────
depenses_data = [
    {'date': aujourd_hui - timedelta(days=2),  'categorie': 'carburant',      'montant': 5000,  'description': 'Carburant mois en cours'},
    {'date': aujourd_hui - timedelta(days=7),  'categorie': 'reparation',     'montant': 8500,  'description': 'Réparation frein Moto Bravo'},
    {'date': aujourd_hui - timedelta(days=10), 'categorie': 'assurance',      'montant': 15000, 'description': 'Renouvellement assurance Moto Alpha'},
    {'date': aujourd_hui - timedelta(days=15), 'categorie': 'administratif',  'montant': 3000,  'description': 'Frais de carte grise'},
    {'date': aujourd_hui - timedelta(days=25), 'categorie': 'personnel',      'montant': 20000, 'description': 'Dépenses personnelles octobre'},
    {'date': aujourd_hui - timedelta(days=30), 'categorie': 'reparation',     'montant': 5000,  'description': 'Crevaison Moto Alpha'},
]
for d in depenses_data:
    dep, created = Depense.objects.get_or_create(
        date=d['date'], description=d['description'],
        defaults=d
    )
    if created: print(f"  💸 Dépense créée : {dep.description}")

# ── ÉPARGNE ────────────────────────────────────────────
epargnes_data = [
    {'date': aujourd_hui - timedelta(days=30), 'montant': 35000, 'description': 'Épargne mois précédent'},
    {'date': aujourd_hui - timedelta(days=60), 'montant': 28000, 'description': 'Épargne mois M-2'},
]
for d in epargnes_data:
    e, created = Epargne.objects.get_or_create(date=d['date'], defaults=d)
    if created: print(f"  🐷 Épargne créée : {e.montant} FCFA")

print("\n✅ Initialisation terminée !")
print("━" * 40)
print("🌐 Démarrer : python manage.py runserver")
print("🔑 Login   : admin / admin123")
print("📍 URL     : http://127.0.0.1:8000/")
print("━" * 40)
