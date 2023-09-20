# Uber driver Assistant for talking with customers, who have disorders

This README file provides a detailed explanation of a Django project for a chatbot that facilitates communication between taxi drivers and customers with psychological disorders. The chatbot leverages advanced Natural Language Processing (NLP) techniques to provide unique advice as a professional psychologist based on given extracted parts of a psychological document and user questions.

## Project Overview

This Django project is designed to provide a web-based interface for users to interact with the chatbot. The chatbot analyzes user input, performs document similarity searches, and generates responses based on a predefined prompt template. The core components of the project include:

- Django: The web framework used to build the project.
- REST Framework: An extension for Django that facilitates the creation of RESTful APIs.
- PyPDF2: A library for extracting text from PDF documents.
- OpenAI: The OpenAI GPT-3 model is used for natural language understanding and generation.
- Langchain: A library that provides various NLP capabilities, including text splitting and vector indexing.
- Faiss: An efficient similarity search library for large-scale text data.

## Prerequisites

Before running the project, ensure you have the following prerequisites installed:

- Python 3.x
- Django
- Rest Framework
- PyPDF2
- OpenAI
- Langchain
- Faiss

You can install most of these dependencies using `pip`.

## Getting Started

1. Clone the repository to your local machine:

   ```shell
   git clone <repository_url>


# Navigate to the project directory:
cd django-psychological-chatbot

# Set your OpenAI API key as an environment variable. Replace "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" with your actual API key.
export OPENAI_API_KEY="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"

# Run the Django development server:
python manage.py runserver


# The server will start, and you can access the chatbot interface at http://localhost:8000.

## Project Structure
The project structure is organized as follows:

- `django_psychological_chatbot`: The Django application folder containing the main project settings.
- `content`: Directory where the PDF document(s) for analysis are stored.
- `langchain`: Custom library for NLP operations, including text splitting and vector indexing.
- `psychological_chatbot`: The Django app that defines the chatbot logic.
- `templates`: HTML templates for rendering the chatbot interface.
- `views.py`: Contains the ChatbotView class, which handles user interactions and AI responses.

## Usage
### API Endpoint
The chatbot is accessible via a RESTful API. You can interact with it by sending POST requests to the following endpoint:

# POST /api/chatbot/
## Request Parameters
- `email`: User's email address.
- `user_input`: User's input text (question or message).

## Example Request
curl -X POST -H "Content-Type: application/json" -d '{"email": "user@example.com", "user_input": "I need advice on managing stress."}' http://localhost:8000/api/chatbot/

## Example Response
{
    "response": "Chatbot response goes here."
}

## Project Customization
You can customize the chatbot's behavior by modifying the code in `views.py`. The key components include:

- **Prompt Template**: Modify the template variable to change the chatbot's response format and behavior.
- **Document Processing**: Update the code related to PDF document processing to use different documents or extraction techniques.
- **OpenAI Configuration**: You can fine-tune the OpenAI settings, such as temperature and chain type, in the ChatbotView class.

## Conclusion
This Django project provides a powerful chatbot interface that can assist users with psychological disorders by offering professional advice based on extracted document content. You can extend and customize the project to meet your specific requirements. Enjoy using and enhancing this chatbot project!
