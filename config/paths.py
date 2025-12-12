import os

#PATH NAMES
BASE_DIRECTORY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#MODEL PATHS
MODEL_DIRECTORY = os.path.join(BASE_DIRECTORY, "Model")
#TO SAVE CLUB DATA
GENERATED_CONTENT_PATH = os.path.join(MODEL_DIRECTORY, "generated_content")
CLUB_DATA_JSON = os.path.join(GENERATED_CONTENT_PATH, "rso.json")

#TO LOAD CLUB DATA
CLUB_INDICES_PATH = os.path.join(GENERATED_CONTENT_PATH, "club_indices.pkl")

#TO LOAD MODELS
TRAINED_MODEL_PATH = os.path.join(GENERATED_CONTENT_PATH, "trained_models")

TFIDF_VECTORIZER_PATH = os.path.join(TRAINED_MODEL_PATH, "tfidf_vectorizer.pkl")
LEXICAL_MATRIX_PATH = os.path.join(TRAINED_MODEL_PATH, "lexical_matrix.npz")

SEMANTIC_MODEL_PATH = os.path.join(TRAINED_MODEL_PATH, "semantic_model") 
SEMANTIC_MATRIX_PATH = os.path.join(TRAINED_MODEL_PATH, "semantic_matrix.npy")

#VIEW PATHS
VIEW_DIRECTORY = os.path.join(BASE_DIRECTORY, "View")

#TO LOAD CSS STYLESHEETS
STATIC_DIRECTORY = os.path.join(VIEW_DIRECTORY, 'static')

#TO LOAD HTML FILES
TEMPLATE_DIRECTORY = os.path.join(VIEW_DIRECTORY, 'templates')