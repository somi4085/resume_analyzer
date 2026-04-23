from sklearn.metrics.pairwise import cosine_similarity

def get_match_Score(vectors):
    score = cosine_similarity(vectors[0],vectors[1])

    return round(score[0][0]*100,2)