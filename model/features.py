from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()

def vectorize(resume, jd):
    vectors = vectorizer.fit_transform([resume, jd])
    
    return vectors