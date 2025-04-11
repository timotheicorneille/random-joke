
# Deployment

## Local Deployment
Pour d�ployer l'application localement, utilisez la commande suivante :
```bash
uvicorn app.main:app --reload
```

## Production Deployment
Pour un d�ploiement en production, il est recommand� d'utiliser un serveur comme Gunicorn avec Uvicorn.
```bash
gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app
```

## CI/CD
Le d�ploiement de la documentation utilisateur est automatis� via GitHub Actions. Le fichier de configuration est situ� dans `.github/workflows/deploy-docs.yml`.
