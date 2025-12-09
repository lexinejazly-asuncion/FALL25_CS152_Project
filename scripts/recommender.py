import pandas as pd
import pickle
import numpy as np

from scipy.sparse import load_npz
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from scripts.process import preprocess

from config.paths import TFIDF_VECTORIZER_PATH, LEXICAL_MATRIX_PATH, SEMANTIC_MODEL_PATH, SEMANTIC_MATRIX_PATH, CLUB_SIMILARITY_MATRIX_PATH

#round1 of recommendations (results show up on explore page): fused ranks from semantic and lexical matching comparing every club against the user query
def recommend(user_input, club_indices, n):
    #load the tdidf vectorizer and lexical matrix
    with open(TFIDF_VECTORIZER_PATH, "rb") as f:
        tfidf_vectorizer = pickle.load(f)
    lexical_club_matrix = load_npz(LEXICAL_MATRIX_PATH)


    #load the sentence embeddings model and semantic matrix
    sentence_embedding_model = SentenceTransformer(SEMANTIC_MODEL_PATH)
    semantic_club_matrix = np.load(SEMANTIC_MATRIX_PATH)

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

#round2 of recommendations (results show up on your recommendations page): from user selected clubs, compute cosine similary comparing with other clubs
def find_similar_clubs(selected_club_names, club_indices, n=10):
    #load the similarity matrix
    similarity_matrix = np.load(CLUB_SIMILARITY_MATRIX_PATH)

    # map club names to their index position in the matrix
    name_to_index = {name: i for i, name in enumerate(club_indices)}
    
    # initialize scores for all clubs
    cumulative_scores = pd.Series(0.0, index=club_indices)
    
    # aggregate similarity scores
    for name in selected_club_names:
        if name in name_to_index:
            idx = name_to_index[name]
            # Get the similarity vector for the selected club
            similarity_vector = similarity_matrix[idx]
            
            # Add to cumulative scores
            club_scores = pd.Series(similarity_vector, index=club_indices)
            cumulative_scores += club_scores
            
    # filter out the selected clubs themselves
    cumulative_scores = cumulative_scores.drop(labels=selected_club_names, errors='ignore')

    # normalize scores and rank
    if not cumulative_scores.empty:
        # normalize by the number of clubs selected
        normalized_scores = cumulative_scores / len(selected_club_names)
        
        # select the top N
        top_n = normalized_scores.sort_values(ascending=False).head(n)
        return top_n.index.tolist()
    
    else:
        return []