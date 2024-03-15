import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from functions import *


origins = ["http://localhost", "http://localhost:8001"]

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/k-means")
def return_kmeans_silhouette_score():
    result_kmeans = kmeans_silhouette_score()
    return {"result": result_kmeans}

@app.get("/spectral")
def return_spectral_silhouette_score():
    result_spectral = spectral_silhouette_score()
    return{"result": result_spectral}

@app.get("/dbscan")
def return_dbscan_silhouette_score():
    result_dbscan = dbscan_silhouette_score()
    return{"result": result_dbscan}


uvicorn.run(app, host="localhost", port=8000)