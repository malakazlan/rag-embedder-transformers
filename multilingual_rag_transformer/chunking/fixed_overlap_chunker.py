def  fixed_length_chunk(sentences, chunk_size=5, overlap=2):
    chunks = []
    i=0
    while i <len(sentences):
        chunk = sentences[i:i+chunk_size]
        chunks.append(" ".join (chunk))
        i+=chunk_size-overlap
    return chunks
 
