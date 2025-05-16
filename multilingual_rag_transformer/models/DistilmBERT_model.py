from sentence_transformers import SentenceTransformer

class DistilmBERTEmbedder:
    def __init__(self, model_name="sentence-transformers/distiluse-base-multilingual-cased-v2"):
        self.model = SentenceTransformer(model_name)

    def embed(self,texts:list[str])-> list[list[float]]:
        formatted = [f"passage: {t}" for t in texts]
        return self.model.encode(formatted,convert_to_numpy=True).tolist()    
