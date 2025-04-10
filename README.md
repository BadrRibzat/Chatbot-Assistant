# Chatbot Assistant

An AI-powered chatbot with a Vue.js frontend and Django backend, deployed on Vercel and Fly.io. It uses MongoDB for data storage and provides a simple, interactive chat experience with user authentication. This project showcases full-stack development, API integration, and cloud deployment skills.

## Features
- **AI Chatbot**: Responds to user messages using pre-trained data stored in MongoDB.
- **User Authentication**: Signup, signin, and signout with token-based auth.
- **Session Management**: Limits guest users to 10 messages, unlimited for authenticated users.
- **Frontend**: Vue.js with Vuex and Vue Router, deployed at `https://chatbot-assistant-frontend.vercel.app`.
- **Backend**: Django REST API with Swagger/ReDoc docs, deployed at `https://chatbot-backend-badr.fly.dev`.
- **Database**: MongoDB for messages and training data.
- **Health Check**: `/chat/health/` endpoint for backend status.

## Tech Stack
- **Frontend**: Vue 3, Vuex, Vue Router, Tailwind CSS, Vercel
- **Backend**: Django 4.2.11, Django REST Framework, Python 3.11, Fly.io
- **Database**: MongoDB (via `pymongo`)
- **API Docs**: `drf-yasg` (Swagger at `/`, ReDoc at `/redoc/`)
- **Dependencies**: See `backend/requirements.txt` and `frontend/package.json`

## Setup Instructions

### Prerequisites
- Node.js 18+ (for frontend)
- Python 3.11+ (for backend)
- MongoDB (local or cloud, e.g., MongoDB Atlas)
- Git
- Vercel CLI (`npm i -g vercel`)
- Fly.io CLI (`flyctl`)

### Local Installation

#### Backend
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/BadrRibzat/Chatbot-Assistant.git
   cd Chatbot-Assistant/backend
2. **Set Up Virtual Environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # Windows: env\Scripts\activate
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
4. **Configure Environment Variables: Create backend/.env**:
   ```bash
   MONGO_URI=mongodb+srv://<user>:<pass>@<cluster>.mongodb.net/?retryWrites=true&w=majority
   SECRET_KEY=<your-secret-key>
   DEBUG=true
5. **Run Migrations**:
   ```bash
   python manage.py migrate
6. **Start Server**:
   ```bash
   python manage.py runserver
-  Access at http://localhost:8000.

#### Frontend
1. **Navigate to Frontend**:
   ```bash
   cd ../frontend
2. **Install Dependencies**:
   ```bash
   npm install
3. **Configure Environment: Create frontend/.env**:
   ```bash
   VUE_APP_BACKEND_URL=http://localhost:8000
4. **Run Locally**:
   ```bash
   vercel dev
-  Access at http://localhost:3000.

#### Deployment
#### Backend on Fly.io
1.  **Login to Fly**:
   ```bash
   flyctl auth login
2.  **Deploy**:
   ```bash
   cd backend
   flyctl deploy

-  URL: https://chatbot-backend-badr.fly.dev.

#### Frontend on Vercel
1.  **Login to Vercel**:
   ```bash
   vercel login
2.  **Deploy**:
   ```bash
   cd frontend
   vercel --prod

-  URL: https://chatbot-assistant-frontend.vercel.app.
-  Set VUE_APP_BACKEND_URL=https://chatbot-backend-badr.fly.dev in Vercel dashboard (Settings > Environment Variables).

#### API Endpoints

-  Health Check: GET /chat/health/ - {"status": "ok"}
-  Chat: POST /chat/ - {"message": "<text>"} (returns {"response": "<reply>", "message_count": <n>})
-  Signup: POST /chat/signup/ - {"username": "<user>", "password": "<pass>"} (returns token)
-  Signin: POST /chat/signin/ - {"username": "<user>", "password": "<pass>"} (returns token)
-  Signout: POST /chat/signout/ - Requires Authorization: Token <token> (logs out)
-  Swagger UI: GET / - Interactive API docs
-  ReDoc: GET /redoc/ - Alternative API docs

#### Example Usage
-  **Chat**:
   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"message": "The kitchen stinks"}' https://chatbot-backend-badr.fly.dev/chat/
-  **Sign Up**:
   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"username": "testuser", "password": "test123"}' https://chatbot-backend-badr.fly.dev/chat/signup/


#### Project Structure
```bash
Chatbot-Assistant/
├── backend/              # Django backend
│   ├── backend/         # Settings and URLs
│   ├── chatbot/         # App logic (views, models, auth)
│   ├── staticfiles/     # Static assets
│   ├── manage.py        # Django management
│   ├── requirements.txt # Backend dependencies
│   ├── fly.toml         # Fly.io config
│   ├── Dockerfile       # Docker setup
│   └── .env             # Backend env vars
├── frontend/             # Vue.js frontend
│   ├── src/             # Vue components, services, store
│   ├── public/          # Static files
│   ├── package.json     # Frontend dependencies
│   ├── vercel.json      # Vercel config
│   └── .env             # Frontend env vars
└── README.md            # Documentation

#### Next Steps
-  AI Enhancement: Integrate BERT or GPT for smarter responses.
-  UI Polish: Add loading states and better error handling in the frontend.
-  Analytics: Log usage metrics in MongoDB.

#### License
-  For demonstration purposes only—not licensed for commercial use.
  **Built by BadrRibzat
