
# Architecture

## Overview
L'application Joke API est construite en utilisant FastAPI, un framework moderne pour construire des APIs avec Python 3.10.

## Components
- **FastAPI**: Framework web pour construire des APIs.
- **Uvicorn**: Serveur ASGI pour servir l'application FastAPI.
- **MkDocs**: G�n�rateur de documentation statique.

## Data Flow
1. L'utilisateur envoie une requ�te � l'API.
2. FastAPI traite la requ�te et appelle les fonctions appropri�es dans `app/jokes.py`.
3. Les r�ponses sont renvoy�es � l'utilisateur en format JSON.
