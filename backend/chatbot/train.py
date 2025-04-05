import json
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from django.conf import settings

nltk.download('punkt')

def train_model():
    db = settings.DB
    training_data = list(db.training_data.find())

    # If no data in MongoDB, load from JSON
    if not training_data:
        with open('data/conversations.json', 'r') as f:
            training_data = json.load(f)
        if training_data:
            db.training_data.insert_many(training_data)
            print(f"Loaded {len(training_data)} entries into training_data collection.")

    inputs = [item["input"] for item in training_data]
    responses = [item["response"] for item in training_data]

    if not inputs:
        print("No training data available. Please populate data/conversations.json.")
        return

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(inputs)

    with open('chatbot/model.pkl', 'wb') as f:
        pickle.dump({'vectorizer': vectorizer, 'tfidf_matrix': tfidf_matrix, 'responses': responses}, f)
    print("Model trained and saved as chatbot/model.pkl.")

if __name__ == "__main__":
    import os
    import django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')  # Changed from 'chatbot_assistant.settings'
    django.setup()
    train_model()
