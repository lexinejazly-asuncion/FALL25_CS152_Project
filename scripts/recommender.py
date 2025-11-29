import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from scripts.process import preprocess

def compute_similarity(club_matrix):
    #finds the similarity between the vectors 
    return cosine_similarity(club_matrix, club_matrix) 

def recommend(user_input, club_indices, sentence_embedding_model, tfidf_vectorizer, sentence_club_matrix, tfidf_club_matrix, n=10):
    #process the query
    processed_query = preprocess(user_input)
    
    #find the similarity between 
    query_semantic_vector = sentence_embedding_model.encode([processed_query]) #transforms text in 'description_keywords' into vectors, represents it semanticallu
    dense_scores = cosine_similarity(query_semantic_vector, sentence_club_matrix)[0] #compute the cosine similarity between the vectors
    dense_ranked = pd.Series(dense_scores, index=club_indices).sort_values(ascending=False)
    
    #find the similarity between 
    query_lexical_vector = tfidf_vectorizer.transform([processed_query]) #transforms text in 'description_keywords' into vectors, represents it lexically
    sparse_scores = cosine_similarity(query_lexical_vector, tfidf_club_matrix)[0] #compute the cosine similarity between the vectors
    sparse_ranked = pd.Series(sparse_scores, index=club_indices).sort_values(ascending=False)
    
    #combine ranked scores using Reciprocal Rank Fusion
    fused_scores = {}
    k = 60 #in rrf implementations, k is typically 60
    
    #process dense Ranks
    for rank, (club_name, score) in enumerate(dense_ranked.items()):
        fused_scores[club_name] = fused_scores.get(club_name, 0) + (1 / (rank + k))

    #process sparse Ranks
    for rank, (club_name, score) in enumerate(sparse_ranked.items()):
        fused_scores[club_name] = fused_scores.get(club_name, 0) + (1 / (rank + k))
        
    #select the top n scored clubs
    top_n = pd.Series(fused_scores).sort_values(ascending=False).head(n)

    return top_n.index.tolist()
