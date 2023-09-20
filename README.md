# Django Chatbot Project

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
