from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import save_message, get_message_count
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the trained model
with open('chatbot/model.pkl', 'rb') as f:
    model_data = pickle.load(f)
    vectorizer = model_data['vectorizer']
    tfidf_matrix = model_data['tfidf_matrix']
    responses = model_data['responses']

@csrf_exempt
def chat(request):
    if not request.session.session_key:
        request.session.create()
        request.session.save()
    
    user_id = request.user.id if request.user.is_authenticated else f"guest_{request.session.session_key}"
    
    if not request.user.is_authenticated:
        message_count = get_message_count(user_id)
        if message_count >= 10:
            return JsonResponse({"error": "Message limit reached. Please sign up or log in."}, status=403)

    if request.method == "POST":
        message = request.POST.get("message", "").strip()
        # Vectorize the input
        message_vector = vectorizer.transform([message])
        # Compute similarity
        similarities = cosine_similarity(message_vector, tfidf_matrix)
        best_match_idx = similarities.argmax()
        similarity_score = similarities[0][best_match_idx]

        # Threshold for a good match (adjust as needed)
        if similarity_score > 0.3:
            response = responses[best_match_idx]
        else:
            response = "I don’t know how to respond to that yet!"
        
        save_message(user_id, message, response)
        return JsonResponse({"response": response})
    return JsonResponse({"error": "Invalid request"}, status=400)
