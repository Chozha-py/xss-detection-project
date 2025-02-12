import joblib
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import csv
data = []
with open("dataset.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header if needed
    for row in reader:
        data.append(row)
# Split dataset
X = data.iloc[:, :-1]  
y = data.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train models
rf_model = RandomForestClassifier().fit(X_train, y_train)
nb_model = MultinomialNB().fit(X_train, y_train)
svm_model = SVC().fit(X_train, y_train)

# Ensure models directory exists
os.makedirs("models", exist_ok=True)

# Save models
joblib.dump(rf_model, "models/xss_rf_model.pkl")
joblib.dump(nb_model, "models/xss_nb_model.pkl")
joblib.dump(svm_model, "models/xss_svm_model.pkl")

print("✅ All models trained and saved!")
