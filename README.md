# Hotel RAG Assistant

## Project Overview

A Retrieval-Augmented Generation (RAG) based AI receptionist that answers guest questions using information from a hotel knowledge base.

## Technologies Used

- pypdf – extracts text from the PDF
- Sentence Transformers – creates embeddings
- ChromaDB – stores and searches vectors
- Groq – generates answers using an LLM
- Streamlit – provides the chat interface

## RAG Flow

```text
PDF
 ↓
Document Loading
 ↓
Chunking
 ↓
Embeddings
 ↓
ChromaDB
 ↓
Retrieval
 ↓
Relevant Context
 ↓
Groq LLM
 ↓
Answer
 ↓
Streamlit UI


## To Run Locally

1. Clone the repository

git clone https://github.com/Nikhila-akaike/hotel-rag-assistant.git
cd hotel-rag-assistant

2. Create and activate a virtual environment

python -m venv .venv
.venv\Scripts\Activate.ps1

3. Install the required packages

pip install -r requirements.txt

4. Configure the Groq API key

Create a .env file in the project root and add:

GROQ_API_KEY=your_groq_api_key

5. Build the vector database

Run the document processing pipeline:

python -m src.pipeline

This loads the hotel PDF, creates chunks, generates embeddings, and stores the vectors for retrieval.

6. Run the application

streamlit run app.py --server.fileWatcherType none

The Streamlit AI receptionist will open in the browser.