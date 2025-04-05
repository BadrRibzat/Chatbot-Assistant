import os
import django
from django.conf import settings

# Configure settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatbot_assistant.settings')
django.setup()

db = settings.DB
collection = db.test_collection
collection.insert_one({"test": "Hello MongoDB from .env"})
print(collection.find_one({"test": "Hello MongoDB from .env"}))
