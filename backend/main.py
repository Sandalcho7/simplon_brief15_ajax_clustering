import uvicorn
import pandas as pd

from fastapi import FastAPI, HTTPException
from sklearn.cluster import KMeans
from sklearn.metrics import mean_squared_error

from config import DATA
from functions import kmeans_inertia


app = FastAPI()


@app.get("/k-means")
def calculate_kmeans_inertia():
    inertia = kmeans_inertia()
    return {"inertia": inertia}



uvicorn.run(app, host="localhost", port=8000)