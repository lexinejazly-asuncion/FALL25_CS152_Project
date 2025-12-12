import pandas as pd
import pickle
import numpy as np
from scipy.sparse import load_npz
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from Model.scripts.process import preprocess
from config.paths import TFIDF_VECTORIZER_PATH, LEXICAL_MATRIX_PATH, SEMANTIC_MODEL_PATH, SEMANTIC_MATRIX_PATH, CLUB_INDICES_PATH

#loads the pre-trained models, matrices, and club indices 
def load_recommendation_models():
    #load the tfidf vectorizer and lexical matrix
    with open(TFIDF_VECTORIZER_PATH, "rb") as f:
        tfidf_vectorizer = pickle.load(f)
    lexical_club_matrix = load_npz(LEXICAL_MATRIX_PATH)

    #load the sentence embeddings model and semantic matrix
    sentence_embedding_model = SentenceTransformer(SEMANTIC_MODEL_PATH)
    semantic_club_matrix = np.load(SEMANTIC_MATRIX_PATH)

    #load club indices (mapping names to matrix positions)
    with open(CLUB_INDICES_PATH, "rb") as f:
        club_indices = pickle.load(f)
        
    return {
        "tfidf_vectorizer": tfidf_vectorizer,
        "lexical_matrix": lexical_club_matrix,
        "semantic_model": sentence_embedding_model,
        "semantic_matrix": semantic_club_matrix,
        "club_indices": club_indices,
    }

#recommendations, results show up on explore page: fused ranks from semantic and lexical matching comparing every club against the user query
def recommend(user_input, loaded_models, n):
    #take the models from the loaded_models dictionary
    tfidf_vectorizer = loaded_models["tfidf_vectorizer"]
    lexical_club_matrix = loaded_models["lexical_matrix"]
    sentence_embedding_model = loaded_models["semantic_model"]
    semantic_club_matrix = loaded_models["semantic_matrix"]
    club_indices = loaded_models["club_indices"]

    #process the query
    processed_query = preprocess(user_input)
    
    #find the similarity between 
    query_semantic_vector = sentence_embedding_model.encode([processed_query]) #transforms text in 'description_keywords' into vectors, represents it semanticallu
    dense_scores = cosine_similarity(query_semantic_vector, semantic_club_matrix)[0] #compute the cosine similarity between the vectors
    dense_ranked = pd.Series(dense_scores, index=club_indices).sort_values(ascending=False)
    
    #find the similarity between 
    query_lexical_vector = tfidf_vectorizer.transform([processed_query]) #transforms text in 'description_keywords' into vectors, represents it lexically
    sparse_scores = cosine_similarity(query_lexical_vector, lexical_club_matrix)[0] #compute the cosine similarity between the vectors
    sparse_ranked = pd.Series(sparse_scores, index=club_indices).sort_values(ascending=False)
    
    #combine ranked scores using Reciprocal Rank Fusion
    fused_scores = {}
    k = 45 #in rrf implementations, k is typically 60, but lower k means more aggressive ranking differences so higher ranked clubs across both models are ranked higher
    
    #process dense Ranks
    for rank, (club_name, score) in enumerate(dense_ranked.items()):
        fused_scores[club_name] = fused_scores.get(club_name, 0) + (1 / (rank + k))

    #process sparse Ranks
    for rank, (club_name, score) in enumerate(sparse_ranked.items()):
        fused_scores[club_name] = fused_scores.get(club_name, 0) + (1 / (rank + k))
        
    #select the top n scored clubs
    top_n = pd.Series(fused_scores).sort_values(ascending=False).head(n)

    return top_n.index.tolist()
