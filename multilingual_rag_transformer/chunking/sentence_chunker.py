def sentence_chunk(sentences, chunk_size=5, overlap=2):
    chunks = []
    for i in range(0, len(sentences), chunk_size - overlap):
        chunk = " ".join(sentences[i:i+chunk_size])
        chunks.append(chunk)
    return chunks
