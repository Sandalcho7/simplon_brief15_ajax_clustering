import uvicorn

from fastapi import FastAPI, HTTPException

from config import DATA
from functions import kmeans_inertia


app = FastAPI()


@app.get("/k-means")
def return_kmeans_inertia():
    inertia = kmeans_inertia()
    return {"inertia": inertia}



uvicorn.run(app, host="localhost", port=8000)