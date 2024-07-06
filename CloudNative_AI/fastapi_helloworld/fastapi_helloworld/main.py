from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"Hello": "World"}

@app.get("/piaic")
def piaic():
    return {"Orginization": "Piaic"}