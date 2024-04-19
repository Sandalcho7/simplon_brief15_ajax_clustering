from scoring import get_dbscan_silhouette_score



def assert_get_dbscan_silhouette_score():
    score = get_dbscan_silhouette_score()
    assert isinstance(score, float), "Expected float, got {}".format(type(score))

assert_get_dbscan_silhouette_score()