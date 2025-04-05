from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import save_message, get_message_count

@csrf_exempt
def chat(request):
    user_id = request.user.id if request.user.is_authenticated else "guest_" + request.session.session_key
    if not request.user.is_authenticated:
        if not request.session.session_key:
            request.session.create()
        message_count = get_message_count(user_id)
        if message_count >= 10:
            return JsonResponse({"error": "Message limit reached. Please sign up or log in."}, status=403)

    if request.method == "POST":
        message = request.POST.get("message", "")
        response = "Echo: " + message  # Placeholder; replace with ML logic later
        save_message(user_id, message, response)
        return JsonResponse({"response": response})
    return JsonResponse({"error": "Invalid request"}, status=400)
