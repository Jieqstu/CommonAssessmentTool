class DummyModel:
    def __init__(self, name, prediction):
        self.name = name
        self.prediction = prediction

    def predict(self, X):
        # Returns a fixed prediction for demonstration purposes
        return [self.prediction] * len(X)