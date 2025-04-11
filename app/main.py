from fastapi import FastAPI
from app.jokes import get_random_joke, submit_joke

app = FastAPI()

@app.get("/random-joke")
def random_joke():
    return {"joke": get_random_joke()}

@app.post("/submit")
def submit(joke: str):
    return submit_joke(joke)
