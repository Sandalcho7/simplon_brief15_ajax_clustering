import matplotlib.pyplot as plt
import io

from fastapi.responses import StreamingResponse

from config import DATA
from processing import format_data



def kmeans_plot(model):
    data = format_data(DATA)
    model.fit(data[["Spending Score (1-100)" , "Annual Income (k$)"]])
    centroids = model.cluster_centers_
    labels = model.labels_

    plt.figure(1, figsize=(15, 7))
    plt.clf()

    plt.scatter(x=data["Spending Score (1-100)"], y=data["Annual Income (k$)"], c=labels, s=200)
    plt.scatter(x=centroids[:, 0], y=centroids[:, 1], s=300, c='red', alpha=0.5)
    plt.ylabel('Spending Score (1-100)')
    plt.xlabel('Annual Income (k$)')

    img_bytes = io.BytesIO()
    plt.savefig(img_bytes, format='png')
    plt.close()

    img_bytes.seek(0)
    return StreamingResponse(img_bytes, media_type="image/png")