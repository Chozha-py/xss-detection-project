import csv
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import word_tokenize
import nltk

nltk.download("punkt")

# Load dataset
dataset_path = "../../data/dataset.csv"

texts = []
labels = []

with open(dataset_path, "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header
    for row in reader:
        if len(row) >= 2:
            texts.append(row[0])  # Assuming the first column is text
            labels.append(int(row[1]))  # Assuming the second column is label (0 or 1)

# Tokenization and TF-IDF Vectorization
def tokenize(text):
    return word_tokenize(text)

vectorizer = TfidfVectorizer(tokenizer=tokenize, lowercase=True)
X = vectorizer.fit_transform(texts)  # Transform the text into vectors

# Save the vectorizer
vectorizer_path = "vectorizer.pkl"
joblib.dump(vectorizer, vectorizer_path)

print(f"Vectorizer saved to {vectorizer_path}")
