from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from data.food import food_items

# load model once
model=SentenceTransformer('all-MiniLM-L6-v2')

# prepare dataset

texts=[f["description"] for f in food_items]
embeddings=model.encode(texts)

# create FAISS index
dimension=embeddings.shape[1]
index=faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

def recommend_food(query:str,k:int=3):
    """Recommend food items based on a query string."""
    query_embedding=model.encode([query])
    distances, indices=index.search(np.array(query_embedding),k)
    recommendations=[food_items[i] for i in indices[0]]
    return recommendations