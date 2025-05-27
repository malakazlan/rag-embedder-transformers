def build_rag_prompt(query: str, retrieved_chunks: list[str]) -> str:
    context = "\n\n".join(retrieved_chunks)
    return f"""You are a multilingual financial assistant. Use the context below to answer the user's question.

Context:
{context}

User Question:
{query}

Answer in the same language. If you don’t know, say "I am not sure about that."
"""
