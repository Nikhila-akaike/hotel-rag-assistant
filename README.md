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