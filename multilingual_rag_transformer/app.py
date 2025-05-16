from data_scraping.scraping import process_pdf_directory, save_texts_by_language
from utils.text_cleaner import preprocess_file
from chunking.fixed_overlap_chunker import fixed_length_chunk
from chunking.sentence_chunker import sentence_chunk
from models.DistilmBERT_model import DistilmBERTEmbedder
from models.mBERT_model import mBERTEmbedder
from models.e5_model import E5Embedder
from config import PINECONE_API_KEY,PINECONE_INDEX_NAME,PINECONE_ENV
from vector_store.pinecone_store import PineconeStore

# def main():
#     # Define the path to your PDF directory
#     pdf_directory = "D:\AGENTS\lang-transformer\multilingual_rag_transformer\data_scraping\pdfs"
    
#     # Process all PDFs in the directory
#     results = process_pdf_directory(pdf_directory)
    
#     # Save English and French texts to data/raw
#     save_texts_by_language(results, "D:/AGENTS/lang-transformer/multilingual_rag_transformer/data/raw")
    
#     # Print results summary
#     print(f"Processed {len(results)} PDF files")
#     for result in results:
#         print(f"\nFile: {result['filename']}")
#         print(f"Content length: {len(result['text_content'])} characters")

import os
RAW_DIR = "multilingual_rag_transformer/data/raw"
PROCESSED_DIR = "D:/AGENTS/lang-transformer/multilingual_rag_transformer/data/processed"

# def preprocess_all_files():
#     for file_name in os.listdir(RAW_DIR):
#         if not file_name.endswith(".txt"):
#             continue

#         input_path = os.path.join(RAW_DIR, file_name)
#         output_path = os.path.join(PROCESSED_DIR, file_name.replace(".txt", "_clean.txt"))

#         print(f"Preprocessing: {file_name}")
#         preprocess_file(input_path, output_path)


# def chunk_demo():
#     for file_name in os.listdir(PROCESSED_DIR):
#         if not file_name.endswith("_clean.txt"):
#             continue

#         print(f"\n Processing: {file_name}")
#         with open(os.path.join(PROCESSED_DIR, file_name), 'r', encoding='utf-8') as f:
#             sentences = [line.strip() for line in f.readlines() if line.strip()]

#         fixed_chunks = fixed_length_chunk(sentences, chunk_size=5, overlap=2)
#         sent_chunks = sentence_chunk(sentences, chunk_size=5)

#         print(f" Fixed Chunks (5, overlap 2): {len(fixed_chunks)}")
#         print(f" Sentence Chunks (5 each): {len(sent_chunks)}")
#         print("Sample Fixed Chunk:\n", fixed_chunks[0][:300])
#         print("Sample Sentence Chunk:\n", sent_chunks[0][:300])



# def embed_chunks_example():
#     DistilmBERT = DistilmBERTEmbedder()
#     mBERT = mBERTEmbedder() 
#     e5 = E5Embedder()

#     for file_name in os.listdir(PROCESSED_DIR):
#         if not file_name.endswith("_clean.txt"):
#             continue

#         with open(os.path.join(PROCESSED_DIR, file_name), 'r', encoding='utf-8') as f:
#             sentences = [line.strip() for line in f.readlines() if line.strip()]

#         chunks = sentence_chunk(sentences, chunk_size=5)

#         print(f"\n Embedding {len(chunks)} chunks from {file_name}")
#         print("DistilmBERT (first vector):", DistilmBERT.embed([chunks[0]])[0][:5])
#         print("dimesion of DistilmBERT:", len(DistilmBERT.embed([chunks[0]])[0]))
#         print("mBERT (first vector):", mBERT.embed([chunks[0]])[0][:5])
#         print("dimesion of mBERT:", len(mBERT.embed([chunks[0]])[0]))
#         print("E5 (first vector):", e5.embed([chunks[0]])[0][:5])
#         print("dimesion of E5:", len(e5.embed([chunks[0]])[0]))


import re
import nltk
from nltk import word_tokenize, pos_tag, ne_chunk
# from nltk.tree import Tree
# nltk.download('maxent_ne_chunker')
# nltk.download('words')
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')


# # --- Date Regex ---
# date_pattern = re.compile(r"\b(?:\d{1,2}(?:st|nd|rd|th)?\s)?(?:January|February|March|April|May|June|July|August|September|October|November|December)\s\d{4}\b")

# def contains_date(text):
#     return bool(date_pattern.search(text))

# # # --- Entity Extractor ---
# def extract_named_entities(text):
#     try:
#         entities = []
#         for sentence in nltk.sent_tokenize(text):
#             tree = ne_chunk(pos_tag(word_tokenize(sentence)))
#             sentence_entities = [" ".join(c[0] for c in subtree) for subtree in tree if isinstance(subtree, Tree)]
#             entities.extend(sentence_entities)
#         return list(set(entities))
#     except:
#         return []
    
# def push_to_pinecone():
#     embedder = mBERTEmbedder()
#     store = PineconeStore(PINECONE_INDEX_NAME, PINECONE_API_KEY, PINECONE_ENV, namespace="cancer_data")


#     for file_name in os.listdir(PROCESSED_DIR):
#         if not file_name.endswith("_clean.txt"):
#             continue

#         with open(os.path.join(PROCESSED_DIR, file_name), 'r', encoding='utf-8') as f:
#             sentences = [line.strip() for line in f.readlines() if line.strip()]

#         chunks = sentence_chunk(sentences, chunk_size=5)
#         embeddings = embedder.embed(chunks)

#         metadata = [
#             {
#                 "source": file_name.replace("_clean.txt", ""),
#                 "chunk_id": i,
#                 "text": chunks[i],
#                 "entities": extract_named_entities(chunks[i]),
#                 "has_date": contains_date(chunks[i])
#     }
#             for i in range(len(chunks))
#         ]

        
#         store.upsert_chunks(chunks, embeddings, metadata)
#         print(f"Uploaded {len(chunks)} chunks from {file_name} to Pinecone.")



def run_similarity_search():
    query = input("\n Enter your medical-related question:\n> ")

    embedder = DistilmBERTEmbedder() 
    store = PineconeStore(
        PINECONE_INDEX_NAME,
        PINECONE_API_KEY,
        PINECONE_ENV,
        namespace="cancer_data"  # your latest namespace
    )

    query_embedding = embedder.embed([f"query: {query}"])[0]

    # filter_metadata = {
    #     "entities": {"$in": ["Sheila A. Stamps"]},
    #     "has_date": True
    # }

    # For debugging: remove filter, get all top_k results
    results = store.search(query_embedding, top_k=5)

    print("\n Top Matching Chunks:")
    if not results.get('matches'):
        print("No matches found.")
    else:
        for match in results['matches']:
            metadata = match['metadata']
            print(f"\n[Score: {match['score']:.4f}] From: {metadata['source']}, Chunk ID: {metadata['chunk_id']}")
            print(f"→ Content Preview: {metadata.get('text', 'N/A')[:300]}")
            print(f"→ Entities: {metadata.get('entities', [])}")
            print(f"→ Has Date: {metadata.get('has_date', False)}")








if __name__ == "__main__":
    # main()
    # preprocess_all_files()
    # chunk_demo()
    # embed_chunks_example()
    # push_to_pinecone()
    run_similarity_search()