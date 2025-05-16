from pinecone import Pinecone,ServerlessSpec
import os

class PineconeStore:
    def __init__(self,index_name,api_key,env_name,namespace=None):
        self.pc = Pinecone(api_key=api_key)
        self.index = self.pc.Index(index_name)
        self.namespace = namespace
    
    def upsert_chunks(self,chunks,embeddings,metadata):
        vectors = [
            {
                "id":f"chunk_{i}",
                "values":embeddings[i],
                "metadata":metadata[i]
            }
            for i in range(len(chunks))
        ]
        upsert_args = {"vectors": vectors}
        if self.namespace:
            upsert_args["namespace"] = self.namespace
        self.index.upsert(**upsert_args)
        
    def search(self,query_vector,top_k=5,filter_metadata=None):
        query_args = {
            "vector":query_vector,
            "top_k":top_k,
            "include_metadata":True
            }
        if filter_metadata:
            query_args["filter"] = filter_metadata
        if self.namespace:
            query_args["namespace"] = self.namespace
        results = self.index.query(**query_args)
        return results
        
        
