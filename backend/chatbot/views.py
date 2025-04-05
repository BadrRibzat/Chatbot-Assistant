from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import save_message, get_message_count
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Load model and tokenizer once at startup
tokenizer = GPT2Tokenizer.from_pretrained('chatbot/model')
model = GPT2LMHeadModel.from_pretrained('chatbot/model')

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
        # Tokenize input and generate response
        inputs = tokenizer.encode(message + " [SEP]", return_tensors="pt")
        outputs = model.generate(inputs, max_length=50, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)
        response = tokenizer.decode(outputs[0], skip_special_tokens=True).split("[SEP]")[1].strip()
        
        save_message(user_id, message, response)
        return JsonResponse({"response": response})
    return JsonResponse({"error": "Invalid request"}, status=400)
