import joblib

class XSSDetector:
    def __init__(self, model_path, vectorizer_path):
        self.model = joblib.load(model_path)
        self.vectorizer = joblib.load(vectorizer_path)
    
    def detect(self, input_text):
        # Preprocess the input text
        X = self.vectorizer.transform([input_text])
        
        # Predict
        prediction = self.model.predict(X)
        return prediction[0]  # 1 for malicious, 0 for benign