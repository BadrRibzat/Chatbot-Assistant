from django.conf import settings
import datetime

def save_message(user_id, message, response):
    collection = settings.DB.messages
    collection.insert_one({
        "user_id": user_id,
        "message": message,
        "response": response,
        "timestamp": datetime.datetime.now()
    })

def get_message_count(user_id):
    collection = settings.DB.messages
    return collection.count_documents({"user_id": user_id})
