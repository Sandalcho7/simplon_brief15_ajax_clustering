import pandas as pd

from sklearn.cluster import KMeans
from config import DATA


def kmeans_inertia():
    model = KMeans(n_clusters=5, n_init="auto")
    model.fit(DATA[["Spending Score (1-100)" , "Annual Income (k$)"]])

    return model.inertia_