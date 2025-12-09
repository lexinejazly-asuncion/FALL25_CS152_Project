import os
import pickle
import numpy as np
from scipy.sparse import save_npz
from sklearn.metrics.pairwise import cosine_similarity

from sklearn.feature_extraction.text import TfidfVectorizer
from sentence_transformers import SentenceTransformer

from config.paths import TFIDF_VECTORIZER_PATH, LEXICAL_MATRIX_PATH, SEMANTIC_MODEL_PATH, SEMANTIC_MATRIX_PATH, CLUB_SIMILARITY_MATRIX_PATH

#create the directories for the file paths
def make_dir(file_path):
    directory = os.path.dirname(file_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
                 
#round1 of recommendations (results show up on explore page): fused ranks from semantic and lexical matching comparing every club against the user query
#round2 of recommendations (results show up on your recommendations page): from user selected clubs, compute cosine similary comparing with other clubs
def train_and_initialize_models(clubs_df):
        #round1
        #1. keyword matching (lexical) query-club comparison
        tfidf_vectorizer = TfidfVectorizer() #initialize a vector, where values are the result of td-idf
        lexical_club_matrix = tfidf_vectorizer.fit_transform(clubs_df["description_keywords"]) #transforms text in 'description_keywords' into vectors, represents it lexically

        make_dir(TFIDF_VECTORIZER_PATH)
        #save the tfidf vectorizer
        with open(TFIDF_VECTORIZER_PATH, 'wb') as f:
            pickle.dump(tfidf_vectorizer, f) 

        make_dir(LEXICAL_MATRIX_PATH)
        save_npz(LEXICAL_MATRIX_PATH, lexical_club_matrix) #save the sparse matrix

        #2. sentence meaning matching (semantic) query-club comparison
        model = SentenceTransformer('all-mpnet-base-v2') #initiaze the Sentence Transformer model
        semantic_club_matrix = model.encode(clubs_df["description_keywords"].tolist()) #transforms text in 'description_keywords' into vectors, represents it semantically
        
        make_dir(SEMANTIC_MODEL_PATH)
        model.save(SEMANTIC_MODEL_PATH)

        make_dir(SEMANTIC_MATRIX_PATH)
        np.save(SEMANTIC_MATRIX_PATH, semantic_club_matrix) #save the dense matrix

        #round2
        #3. hybrid (lexical and semantic) matching club-club comparison 
        similarity_matrix = cosine_similarity(semantic_club_matrix, semantic_club_matrix) 
        np.save(CLUB_SIMILARITY_MATRIX_PATH, similarity_matrix)


