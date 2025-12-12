import os
import pickle
import numpy as np
from scipy.sparse import save_npz
from sklearn.feature_extraction.text import TfidfVectorizer
from sentence_transformers import SentenceTransformer

from config.paths import TFIDF_VECTORIZER_PATH, LEXICAL_MATRIX_PATH, SEMANTIC_MODEL_PATH, SEMANTIC_MATRIX_PATH, CLUB_INDICES_PATH

#create the directories for the file paths
def make_dir(file_path):
    directory = os.path.dirname(file_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
                 
#recommendations, results show up on explore page: fused ranks from semantic and lexical matching comparing every club against the user query
def train_and_initialize_models(clubs_df):

        #indices to map vectors to 
        club_indices = clubs_df.index.tolist()
        make_dir(CLUB_INDICES_PATH)
        #save club indices
        with open(CLUB_INDICES_PATH, 'wb') as f:
            pickle.dump(club_indices, f)

        #1. keyword matching (lexical) query-club comparison
        tfidf_vectorizer = TfidfVectorizer() #initialize a vector, where values are the result of td-idf
        lexical_club_matrix = tfidf_vectorizer.fit_transform(clubs_df["description_keywords"]) #calculates idf weights, transforms text in 'description_keywords' into vectors, represents it lexically

        make_dir(TFIDF_VECTORIZER_PATH)
        #save the tfidf vectorizer
        with open(TFIDF_VECTORIZER_PATH, 'wb') as f:
            pickle.dump(tfidf_vectorizer, f) 

        make_dir(LEXICAL_MATRIX_PATH)
        save_npz(LEXICAL_MATRIX_PATH, lexical_club_matrix) #save the sparse matrix

        #2. sentence meaning matching (semantic) query-club comparison
        model = SentenceTransformer('all-MiniLM-L12-v2') #initiaze the Sentence Transformer model
        semantic_club_matrix = model.encode(clubs_df["description_keywords"].tolist()) #calcuates embeddings, transforms text in 'description_keywords' into vectors, represents it semantically
        
        make_dir(SEMANTIC_MODEL_PATH)
        model.save(SEMANTIC_MODEL_PATH)

        make_dir(SEMANTIC_MATRIX_PATH)
        np.save(SEMANTIC_MATRIX_PATH, semantic_club_matrix) #save the dense matrix


