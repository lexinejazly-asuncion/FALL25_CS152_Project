import os

#PATH NAMES
BASE_DIRECTORY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

GENERATED_CONTENT_PATH = os.path.join(BASE_DIRECTORY, "generated_content")
CLUB_DATA_JSON = os.path.join(GENERATED_CONTENT_PATH, "rso.json")

#TO LOAD MODELS
MODEL_PATH = os.path.join(GENERATED_CONTENT_PATH, "models")

CLUB_SIMILARITY_MATRIX_PATH = os.path.join(MODEL_PATH, "club_similarity_matrix.npy")

TFIDF_VECTORIZER_PATH = os.path.join(MODEL_PATH, "tfidf_vectorizer.pkl")
LEXICAL_MATRIX_PATH = os.path.join(MODEL_PATH, "lexical_matrix.npz")

SEMANTIC_MODEL_PATH = os.path.join(MODEL_PATH, "semantic_model") 
SEMANTIC_MATRIX_PATH = os.path.join(MODEL_PATH, "semantic_matrix.npy")