from django.conf import settings
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import save_message, get_message_count

@api_view(['POST'])
@permission_classes([AllowAny])
def chat(request):
    if not request.session.session_key:
        request.session.create()
        request.session.save()
    
    user_id = request.user.id if request.user.is_authenticated else f"guest_{request.session.session_key}"
    
    if not request.user.is_authenticated:
        message_count = get_message_count(user_id)
        if message_count >= 10:
            return Response({
                "error": "Message limit reached. Please sign up for unlimited messages.",
                "signup_url": "/chat/signup/"
            }, status=403)

    message = request.data.get("message", "").strip()
    if not message:
        return Response({"error": "Message is required"}, status=400)
    
    response = f"Echo: {message}"  # Mock response
    save_message(user_id, message, response)
    return Response({"response": response})
