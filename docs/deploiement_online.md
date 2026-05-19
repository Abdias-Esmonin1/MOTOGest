# Déploiement en ligne de MotoGest

Cette version permet à l'APK Android de fonctionner sans que le PC lance `runserver`.

## 1. Mettre le projet sur GitHub

Crée un dépôt GitHub puis envoie ce projet dessus. L'hébergeur récupérera le code depuis GitHub.

## 2. Créer le service web

Sur l'hébergeur, crée un service web Python avec:

- Build command: `bash build.sh`
- Start command: `gunicorn config.wsgi:application`
- Python: `3.11.9`

## 3. Ajouter PostgreSQL

Crée une base PostgreSQL et mets son URL dans la variable:

```text
DATABASE_URL
```

## 4. Variables d'environnement

Ajoute ces variables:

```text
SECRET_KEY=une-longue-cle-secrete
DEBUG=False
ALLOWED_HOSTS=ton-domaine.com
CSRF_TRUSTED_ORIGINS=https://ton-domaine.com
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
SECURE_SSL_REDIRECT=False
ADMIN_USERNAME=Zadmin
ADMIN_PASSWORD=MMDR
ADMIN_EMAIL=admin@motogest.ci
```

Si l'adresse donnée par l'hébergeur est `https://motogest.onrender.com`, utilise:

```text
ALLOWED_HOSTS=motogest.onrender.com
CSRF_TRUSTED_ORIGINS=https://motogest.onrender.com
```

## 5. Recompiler l'APK

Quand l'adresse en ligne fonctionne, remplace l'URL dans:

```text
mobile_android/app/src/main/res/values/strings.xml
```

Puis recompile l'APK. L'application Android ouvrira l'adresse en ligne et ne dépendra plus du PC.
