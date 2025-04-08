from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from .models import save_message, get_message_count
import re

@api_view(['POST'])
def chat(request):
    user_id = request.user.id if request.user.is_authenticated else "anonymous"
    message = request.data.get('message', '').strip()

    if not message:
        return Response({"response": "Please send a message!"}, status=400)

    # Query training data for a response
    collection = settings.DB.training_data
    # Case-insensitive match with basic normalization
    normalized_message = re.sub(r'[^\w\s]', '', message.lower())
    
    # Exact match first
    result = collection.find_one({"input": {"$regex": f"^{re.escape(message)}$", "$options": "i"}})
    if result:
        response = result['response']
    else:
        # Fallback: partial match or default
        result = collection.find_one({"input": {"$regex": normalized_message, "$options": "i"}})
        response = result['response'] if result else "Sorry, I don’t know how to respond to that yet!"

    save_message(user_id, message, response)
    message_count = get_message_count(user_id)

    return Response({
        "response": response,
        "message_count": message_count
    })

@api_view(['GET'])
def health(request):
    return Response({"status": "ok"}, status=200)
