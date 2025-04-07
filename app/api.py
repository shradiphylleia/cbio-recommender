from typing import Union
from fastapi import FastAPI

from recommender import recommeder_similar_patients

app=FastAPI()

@app.get("/")
def landing():
    return {'cbio':'gsoc_2025'}

@app.get('/similar_patients')
def get_similar_patients():
    return recommeder_similar_patients()

# @app.get('/')