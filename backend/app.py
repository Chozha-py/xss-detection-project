from flask import Flask, request, jsonify
from flask_cors import CORS  # To handle CORS (Cross-Origin Resource Sharing)
from werkzeug.exceptions import BadRequest
import joblib
import nltk
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import bleach  # Import Bleach for sanitization
import os

# Get the absolute path of the model files
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Get the current directory of app.py

MODEL_PATH = os.path.join(os.getcwd(), "models", "xss_model.pkl")

VECTORIZER_PATH = os.path.join(BASE_DIR, "models", "vectorizer.pkl")

# Load the pre-trained machine learning model and vectorizer
model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)


# Initialize Flask app
app = Flask(__name__)

# Enable CORS to allow requests from the frontend
CORS(app)

@app.route("/")
def home():
    return jsonify({"message": "XSS Detection API is running!"})

@app.route("/detect", methods=["POST"])
def detect_xss():
    try:
        # Parse JSON data from request
        data = request.get_json()
        user_input = data.get("input", "")
        
        if not user_input:
            raise BadRequest("Input is required.")
        
        # Sanitize the input using Bleach
        sanitized_input = sanitize_input(user_input)
        
        # Predict if the input is malicious
        is_malicious = predict_xss(user_input)
        
        # Return the result as a JSON response
        return jsonify({
            "input": user_input,
            "sanitized_input": sanitized_input,
            "is_malicious": is_malicious
        })
    
    except BadRequest as e:
        return jsonify({"error": str(e)}), 400

# Function to sanitize the input text using Bleach
def sanitize_input(input_text):
    # Clean the input using bleach to remove dangerous HTML elements
    sanitized = bleach.clean(input_text)
    return sanitized

# Function to predict XSS attack using the model
def predict_xss(input_text):
    # Tokenize and vectorize the input text
    tokens = word_tokenize(input_text)
    vectorized_input = vectorizer.transform([" ".join(tokens)])
    
    # Predict using the trained model
    prediction = model.predict(vectorized_input)
    
    # Return True (malicious) or False (benign)
    return bool(prediction[0])

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
