import uvicorn

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from functions import kmeans_inertia



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
def return_kmeans_inertia():
    inertia = kmeans_inertia()
    return {"inertia": inertia}



uvicorn.run(app, host="localhost", port=8000)