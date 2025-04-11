
# Deployment

## Local Deployment
Pour déployer l'application localement, utilisez la commande suivante :
```bash
uvicorn app.main:app --reload
```

## Production Deployment
Pour un déploiement en production, il est recommandé d'utiliser un serveur comme Gunicorn avec Uvicorn.
```bash
gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app
```

## CI/CD
Le déploiement de la documentation utilisateur est automatisé via GitHub Actions. Le fichier de configuration est situé dans `.github/workflows/deploy-docs.yml`.
