from sklearn.cluster import KMeans, SpectralClustering, DBSCAN
from sklearn.metrics import silhouette_score

from config import DATA


DATA["Gender"] = DATA["Gender"].replace({"Male": 0, "Female": 1})


def kmeans_silhouette_score():
    model = KMeans(n_clusters=5, n_init="auto")
    model.fit(DATA[["Spending Score (1-100)", "Annual Income (k$)"]])

    labels = model.labels_

    silhouette_score_avg = silhouette_score(DATA, labels)

    return silhouette_score_avg


def spectral_silhouette_score():
    model = SpectralClustering(n_clusters=6, n_init=20)
    model.fit(DATA[["Spending Score (1-100)", "Annual Income (k$)"]])

    labels = model.labels_

    silhouette_score_avg = silhouette_score(DATA, labels)

    return silhouette_score_avg


def dbscan_silhouette_score():
    model = DBSCAN(eps=9, min_samples=3)
    model.fit(DATA[["Spending Score (1-100)", "Annual Income (k$)"]])

    labels = model.labels_

    silhouette_score_avg = silhouette_score(DATA, labels)

    return silhouette_score_avg