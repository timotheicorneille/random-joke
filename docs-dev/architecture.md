
# Architecture

## Overview
L'application Joke API est construite en utilisant FastAPI, un framework moderne pour construire des APIs avec Python 3.10.

## Components
- **FastAPI**: Framework web pour construire des APIs.
- **Uvicorn**: Serveur ASGI pour servir l'application FastAPI.
- **MkDocs**: Générateur de documentation statique.

## Data Flow
1. L'utilisateur envoie une requête à l'API.
2. FastAPI traite la requête et appelle les fonctions appropriées dans `app/jokes.py`.
3. Les réponses sont renvoyées à l'utilisateur en format JSON.
