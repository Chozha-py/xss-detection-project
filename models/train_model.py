import os
import csv
import joblib
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences



# Set paths
dataset_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/dataset.csv"))
vectorizer_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "vectorizer.pkl"))
sklearn_model_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "xss_model.pkl"))
tf_model_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "xss_model.h5"))

# Load dataset
if not os.path.exists(dataset_path):
    raise FileNotFoundError(f"Dataset not found: {dataset_path}")

texts, labels = [], []
with open(dataset_path, "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header if present
    for row in reader:
        texts.append(row[0])  # Assuming first column is the text
        labels.append(int(row[1]))  # Assuming second column is the label

# Convert to NumPy arrays
labels = np.array(labels)

# -------------------------
# Scikit-learn Model (RandomForest)
# -------------------------
vectorizer = TfidfVectorizer()
X_sklearn = vectorizer.fit_transform(texts)

# Train model
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_sklearn, labels)

# Save model & vectorizer
joblib.dump(rf_model, sklearn_model_path)
joblib.dump(vectorizer, vectorizer_path)
print("Scikit-learn model trained and saved.")

# -------------------------
# TensorFlow Model (Deep Learning)
# -------------------------
tokenizer = Tokenizer(num_words=5000, oov_token="<OOV>")
tokenizer.fit_on_texts(texts)
X_tf = tokenizer.texts_to_sequences(texts)
X_tf = pad_sequences(X_tf, maxlen=100)

# Define simple neural network
tf_model = tf.keras.Sequential([
   tf.keras.layers.Embedding(5000, 32),
    tf.keras.layers.LSTM(64, return_sequences=True),
    tf.keras.layers.LSTM(32),
    tf.keras.layers.Dense(32, activation="relu"),
    tf.keras.layers.Dense(1, activation="sigmoid")
])

tf_model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
tf_model.fit(X_tf, labels, epochs=5, batch_size=32)

# Save model
tf_model.save(tf_model_path.replace(".h5", ".keras"))
print("TensorFlow model trained and saved.")
