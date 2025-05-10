from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import IsolationForest

class AnomalyDetector:
    def __init__(self):
        self.vectorizer = CountVectorizer()
        self.model = IsolationForest(contamination=0.2)

    def train(self, logs):
        X = self.vectorizer.fit_transform(logs['event'])
        self.model.fit(X)

    def predict(self, logs):
        X = self.vectorizer.transform(logs['event'])
        logs['anomaly'] = self.model.predict(X)
        logs['anomaly'] = logs['anomaly'].map({1: 'Normal', -1: 'Anomaly'})
        return logs
