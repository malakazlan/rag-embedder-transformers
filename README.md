# Multilingual RAG Transformer

A robust pipeline for multilingual Retrieval-Augmented Generation (RAG) using transformer models. This project is designed to process, clean, chunk, embed, and store multilingual documents, supporting advanced search and retrieval tasks in multiple languages.

## Features
- **Multilingual Document Processing:** Handles raw PDFs and text files in various languages.
- **Text Cleaning & Preprocessing:** Language-specific cleaning and sentence tokenization.
- **Chunking Strategies:** Fixed-length and sentence-based chunking for flexible context windows.
- **Transformer Embeddings:** Supports models like DistilmBERT, mBERT, and E5 for embedding text.
- **Vector Store Integration:** Pinecone and MongoDB support for storing and searching embeddings.
- **Extensible Utilities:** Helper functions for language detection, cleaning, and more.

## Folder Structure
```
multilingual_rag_transformer/
│
├── data/                          # Raw and cleaned multilingual documents
│   ├── raw/                      # Original PDFs, TXT, etc.
│   └── processed/                # Cleaned and parsed text files
│
├── embeddings/                   # Saved embeddings (optional for testing)
│
├── models/                       # Scripts to load and use transformer models
│   ├── mBERT_model.py
│   ├── DistilmBERT_model.py
│   └── e5_model.py
│
├── chunking/                     # Chunking strategies
│   ├── sentence_chunker.py
│   └── fixed_overlap_chunker.py
│
├── vector_store/                 # Pinecone or MongoDB integration
│   ├── pinecone_store.py
│   └── mongo_store.py
│
├── utils/                        # Common helper functions
│   ├── text_cleaner.py
│   └── language_utils.py
│
├── screenshots/                  # Screenshots for similarity search results
│
├── app.py                        # Main driver script
├── config.py                     # Store API keys, model names, chunk size etc.
├── requirements.txt              # Dependencies
└── README.md                     # Project description
```

## Main Workflow
1. **Data Ingestion:** Place raw documents in `data/raw/`.
2. **Preprocessing:** Clean and tokenize text using `utils/text_cleaner.py`.
3. **Chunking:** Split text into chunks using `chunking/` modules.
4. **Embedding:** Generate embeddings with transformer models in `models/`.
5. **Vector Storage:** Store and search embeddings using `vector_store/`.
6. **Application:** Use `app.py` to run the full pipeline or demo tasks.

## Transformer Models Used
- **DistilmBERT**: Lightweight BERT variant for fast, multilingual embeddings.
- **mBERT**: Multilingual BERT for robust cross-lingual tasks.
- **E5**: Embedding model for efficient retrieval.

## Getting Started
1. Clone the repo and set up a Python virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Place your documents in `data/raw/` and run the pipeline via `app.py`.

## License
MIT License

---
For more details, see the code and comments in each module.
