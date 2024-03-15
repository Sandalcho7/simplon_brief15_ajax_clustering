from sklearn.metrics import silhouette_score

from config import DATA
from processing import format_data



def kmeans_silhouette_score(model):
    format_data(DATA)
    model.fit(DATA[["Spending Score (1-100)", "Annual Income (k$)"]])

    labels = model.labels_

    silhouette_score_avg = silhouette_score(DATA, labels)

    return silhouette_score_avg


def spectral_silhouette_score(model):
    format_data(DATA)
    model.fit(DATA[["Spending Score (1-100)", "Annual Income (k$)"]])

    labels = model.labels_

    silhouette_score_avg = silhouette_score(DATA, labels)

    return silhouette_score_avg


def dbscan_silhouette_score(model):
    format_data(DATA)
    model.fit(DATA[["Spending Score (1-100)", "Annual Income (k$)"]])

    labels = model.labels_

    silhouette_score_avg = silhouette_score(DATA, labels)

    return silhouette_score_avg