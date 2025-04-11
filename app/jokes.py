# app/jokes.py

from typing import List
import random

# Blagues stockées en mémoire (pour l'exemple)
_jokes: List[str] = [
    "Pourquoi les canards ont-ils autant de plumes ? Pour couvrir leur derrière !",
    "Quel est le comble pour un électricien ? De ne pas être au courant.",
    "Je connais une blague sur les salades... mais elle est un peu verte."
]

def get_random_joke() -> str:
    return random.choice(_jokes)

def submit_joke(joke: str) -> dict:
    _jokes.append(joke)
    return {"message": "Joke added!", "total": len(_jokes)}
