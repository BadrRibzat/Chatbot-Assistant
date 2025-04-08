# Chatbot Assistant

This is an AI-powered chatbot assistant built with Django, leveraging machine learning techniques (TF-IDF with scikit-learn) and MongoDB for data storage. The project demonstrates my skills in developing AI chatbot solutions tailored to client requirements, integrating natural language processing (NLP) and web development. It’s deployed on Fly.io with REST API documentation via Swagger and ReDoc.

## Features
- **AI Chatbot**: Responds to user messages using a pre-trained TF-IDF model.
- **Session Management**: Limits guest users to 10 messages, encouraging authentication.
- **MongoDB Integration**: Stores messages and training data in a NoSQL database.
- **Django Backend**: Provides a robust web framework for API endpoints.
- **API Documentation**: Swagger (`/`) and ReDoc (`/redoc/`) for easy exploration.
- **Health Check**: `/chat/health/` endpoint to monitor app status.
- **Deployed on Fly.io**: Accessible at `https://chatbot-backend-badr.fly.dev/`.
- **Extensible**: Ready for enhancements with TensorFlow, Transformers, or other ML frameworks.

## Tech Stack
- **Backend**: Django 4.2.11, Python 3.11
- **Database**: MongoDB (via pymongo)
- **Machine Learning**: scikit-learn (TF-IDF), NLTK
- **API Tools**: Django REST Framework, drf-yasg (Swagger/ReDoc)
- **Deployment**: Fly.io (via `fly.toml` and Docker)
- **Dependencies**: See `backend/requirements.txt` (e.g., `gunicorn`, `django-cors-headers`)

## Setup Instructions

### Prerequisites
- Python 3.11+
- MongoDB (local or cloud, e.g., MongoDB Atlas)
- Git
- Fly.io CLI (`flyctl`)

### Local Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/BadrRibzat/Chatbot-Assistant.git
   cd Chatbot-Assistant/backend

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt

4. **Configure Environment Variables: Create a .env file in backend/ with your values**:
   ```bash

5. **Run Migrations**:
   ```bash
   python manage.py migrate

6. **Run the Server**:
   ```bash
   python manage.py runserver

### Access the API at http://localhost:8000/.

### Deployment on Fly.io

1. **Install Fly CLI: Follow Fly.io’s installation guide**.

2. **Login to Fly**:
   ```bash
   flyctl auth login

3. **Deploy: From backend/**:
   ```bash
   flyctl deploy

. Uses fly.toml and Dockerfile to build and deploy.
. App runs at https://chatbot-backend-badr.fly.dev/.

4. **Create a Superuser (optional)**:
   ```bash
   flyctl ssh console -a chatbot-backend-badr
   python manage.py createsuperuser

### API Endpoints

. Health Check: GET /chat/health/ - Returns {"status": "ok"}.
. Chat: POST /chat/ - Send message=<text> to get a response (e.g., {"response": "Echo: <text>"}).
. Guests limited to 10 messages.
. Sign In: POST /chat/signin/ - Authenticate with username=<user>&password=<pass>.
. Sign Up: POST /chat/signup/ - Not implemented yet (501 Not Implemented).
. Sign Out: POST /chat/signout/ - Logs out the user.
. Swagger UI: GET / - Interactive API documentation.
. ReDoc: GET /redoc/ - Alternative API documentation.

### Example Usage
. **Health Check**:
   ```bash
   curl https://chatbot-backend-badr.fly.dev/chat/health/

. **Chat as Guest**:
   ```bash
   curl -X POST -d "message=Hello" https://chatbot-backend-badr.fly.dev/chat/

. **Sign In**:
   ```bash
   curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "username=Badr&password=14121990" https://chatbot-backend-badr.fly.dev/chat/signin/

### Project Structure
   ```bash
   Chatbot-Assistant/
   ├── backend/              # Django project root
   │   ├── backend/         # Settings and URLs
   │   ├── chatbot/         # Chatbot app (models, views, auth)
   │   ├── staticfiles/     # Collected static assets
   │   ├── manage.py        # Django management script
   │   ├── requirements.txt # Python dependencies
   │   ├── fly.toml         # Fly.io configuration
   │   ├── Dockerfile       # Docker build instructions
   │   └── .env             # Environment variables
   └── README.md            # Project documentation

### Next Steps

. **Frontend: Build a UI (e.g., React, Vue) and deploy on Netlify, updating CORS_ALLOWED_ORIGINS**.

. **Enhance AI: Integrate Transformers (e.g., BERT) for better NLP responses**.

. **Signup: Implement user registration in chatbot/auth_views.py**.

. **Monitoring: Add logging and analytics for usage tracking**.

### License

. **This project is for demonstration purposes and not licensed for commercial use**.

