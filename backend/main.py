import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sklearn.cluster import KMeans, SpectralClustering, DBSCAN

from models import *
from plots import *

origins = ["http://localhost", "http://localhost:8001"]

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


kmeans_model = KMeans(n_clusters=5, n_init="auto")
spectral_model = SpectralClustering(n_clusters=6, n_init=20)
dbscan_model = DBSCAN(eps=9, min_samples=3)


@app.get("/k-means/score")
def return_kmeans_silhouette_score():
    result_kmeans = kmeans_silhouette_score(kmeans_model)
    return {"result": result_kmeans}

@app.get("/k-means/plot")
def return_kmeans_plot():
    plot_kmeans = kmeans_plot(kmeans_model)
    return {"plot": plot_kmeans}


@app.get("/spectral/score")
def return_spectral_silhouette_score():
    result_spectral = spectral_silhouette_score()
    return{"result": result_spectral}


@app.get("/dbscan/score")
def return_dbscan_silhouette_score():
    result_dbscan = dbscan_silhouette_score()
    return{"result": result_dbscan}



uvicorn.run(app, host="localhost", port=8000)