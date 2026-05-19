# Guide d'installation — MotoGest v1.0

## Prérequis
- Python 3.10+
- pip
- MySQL 8+ (ou SQLite pour développement — déjà configuré)

## Installation rapide

```bash
# 1. Extraire le projet
unzip motogest.zip
cd moto_transport

# 2. Créer un environnement virtuel
python -m venv venv
source venv/bin/activate        # Linux / Mac
venv\Scripts\activate           # Windows

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Configuration (optionnel — SQLite fonctionne sans)
# Éditer .env si vous souhaitez utiliser MySQL

# 5. Appliquer les migrations
python manage.py migrate

# 6. Charger les données de démonstration
python setup_demo.py

# 7. Lancer le serveur
python manage.py runserver
```

## Accès
- URL : http://127.0.0.1:8000/
- Login : **admin**
- Mot de passe : **admin123**

> ⚠️ Changez le mot de passe en production via : `python manage.py changepassword admin`

## Configuration MySQL (production)

Dans `.env` :
```
DB_NAME=moto_transport_db
DB_USER=root
DB_PASSWORD=votre_mot_de_passe
DB_HOST=localhost
DB_PORT=3306
```

Dans `config/settings.py`, décommenter le bloc MySQL et commenter le bloc SQLite.

Créer la base :
```sql
CREATE DATABASE moto_transport_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

## Modules disponibles (v1.0)
| Module | URL | Description |
|---|---|---|
| Dashboard | /dashboard/ | Vue d'ensemble |
| Saisie du jour | /paiements/ | Paiements journaliers |
| Motos | /motos/ | CRUD motos |
| Conducteurs | /conducteurs/ | CRUD conducteurs |
| Pannes | /pannes/ | Déclaration pannes |
| Maintenance | /maintenance/ | Planification entretien |
| Finances | /finances/ | Recettes / Dépenses |
| Répartition | /finances/repartition/ | 35/25/20/20 |
| Rapports | /rapports/ | Export Excel & PDF |
