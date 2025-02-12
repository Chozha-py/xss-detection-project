import pandas as pd
import re
import nltk
from nltk.tokenize import word_tokenize

nltk.download("punkt")

def clean_text(text):
    """Basic text cleaning: remove special characters and tokenize."""
    text = re.sub(r"<.*?>", "", text)  # Remove HTML tags
    text = re.sub(r"[^a-zA-Z0-9 ]", "", text)  # Remove special chars
    tokens = word_tokenize(text.lower())  # Tokenize
    return " ".join(tokens)

def load_data(filepath):
    """Load CSV data and preprocess."""
    df = pd.read_csv(filepath)
    df["clean_text"] = df["text"].apply(clean_text)
    return df
