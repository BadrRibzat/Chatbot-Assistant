# Chatbot Assistant

This is an AI-powered chatbot assistant built with Django, leveraging machine learning techniques (TF-IDF with scikit-learn) and MongoDB for data storage. The project demonstrates my skills in developing AI chatbot solutions tailored to client requirements, integrating natural language processing (NLP) and web development.

## Features
- **AI Chatbot**: Responds to user messages using a pre-trained TF-IDF model.
- **Session Management**: Limits guest users to 10 messages, encouraging authentication.
- **MongoDB Integration**: Stores messages and training data in a NoSQL database.
- **Django Backend**: Provides a robust web framework for API endpoints.
- **Extensible**: Ready for enhancements with TensorFlow, Transformers, or other ML frameworks.

## Tech Stack
- **Backend**: Django 4.2.11, Python 3.11
- **Database**: MongoDB (via pymongo)
- **Machine Learning**: scikit-learn (TF-IDF), NLTK
- **Dependencies**: See `requirements.txt` for full list (e.g., NumPy, Transformers)

## Setup Instructions

### Prerequisites
- Python 3.11+
- MongoDB (local or cloud instance, e.g., MongoDB Atlas)
- Git

### Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/Chatbot-Assistant.git
   cd Chatbot-Assistant

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate

3. **Install Dependencies**:
   ```bash
   pip install -r backend/requirements.txt

4. **Configure Environment Variables**: 
Create a .env file in the backend/ directory with:
   ```bash
   MONGO_URI=mongodb+srv://<username>:<password>@<cluster>.mongodb.net/?retryWrites=true&w=majority
   SECRET_KEY=<your-secret-key>
   DEBUG=true

Replace <username>, <password>, <cluster>, and <your-secret-key> with your own values.

5. **Initialize MongoDB**:
   ```bash
   python backend/manage.py init_db

6. **Load Training Data (optional)**:
   ```bash
   python backend/manage.py load_training_data

7. **Train the Model**:
   ```bash
   python backend/chatbot/train.py

8. **Run the Server**:
   ```bash
   python backend/manage.py runserver

Access the chatbot API at http://localhost:8000/chat/.

### Usage

Send a POST request to /chat/ with a message field to get a response:
   ```bash
   curl -X POST -d "message=Hello" http://localhost:8000/chat/

Guest users are limited to 10 messages; authenticated users have unlimited access.

### Project Structure
   ```bash
   Chatbot-Assistant/
├── backend/              # Django project root
│   ├── backend/         # Django settings and URLs
│   ├── chatbot/         # Chatbot app (models, views, training)
│   ├── data/            # Training data (e.g., conversations.json)
│   ├── manage.py        # Django management script
│   └── requirements.txt # Python dependencies
└── README.md            # Project documentation

Next Steps
Add user authentication and frontend interface.
Enhance the model with Transformers (e.g., BERT) for better NLP.
Deploy to a cloud platform (e.g., Heroku, AWS).

### License
This project is for demonstration purposes and not licensed for commercial use.
   ```bash

**Explanation:**
- **Overview**: Describes the project and its purpose.
- **Features**: Highlights key functionalities.
- **Tech Stack**: Lists the main technologies used.
- **Setup Instructions**: Provides clear steps to get the project running.
- **Usage**: Shows how to interact with the chatbot API.
- **Project Structure**: Outlines the directory layout.
- **Next Steps**: Suggests potential improvements.

---
