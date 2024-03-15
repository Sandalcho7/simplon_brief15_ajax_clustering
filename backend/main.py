import uvicorn
import pandas as pd

from fastapi import FastAPI, HTTPException

from config import DATA
from functions import kmeans_silhouette_score, spectral_silhouette_score, dbscan_silhouette_score

app = FastAPI()

@app.get("/k-means")
def return_kmeans_silhouette_score():
    result_kmeans = kmeans_silhouette_score()
    return {"silhouette_kmeans": result_kmeans}

@app.get("/spectral")
def return_spectral_silhouette_score():
    result_spectral = spectral_silhouette_score()
    return{"silhouette_spectral": result_spectral}

@app.get("/dbscan")
def return_dbscan_silhouette_score():
    result_dbscan = dbscan_silhouette_score()
    return{"silhouette_dbscan": result_dbscan}

uvicorn.run(app, host="localhost", port=8000)
