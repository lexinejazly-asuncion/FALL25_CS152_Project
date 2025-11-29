from sklearn.feature_extraction.text import TfidfVectorizer
from sentence_transformers import SentenceTransformer

from scripts.scrape_web import scrape
from scripts.load import load_clubs, json_to_dframe
from scripts.process import preprocess
from scripts.recommender import recommend
from config.paths import GENERATED_CONTENT_CLUB_PATH

def main():

    print("1. Scraping website")
    scrape() #call scrape method to get information about clubs

    print("2. Loading into dframe")
    clubs = load_clubs(GENERATED_CONTENT_CLUB_PATH) #load the data scraped about clubs
    clubs_df = json_to_dframe(clubs) #create a dframe from the loaded data

    print("3. Selecting keywords from club descriptions")
    clubs_df["description_keywords"] = clubs_df["description"].apply(preprocess) #takes only important words from mission and benefits
    club_indices = clubs_df.index.tolist()

    print("4. Creating vector embeddings")
    tfidf_vectorizer = TfidfVectorizer() #initialize a vector, where values are the result of td-idf
    lexical_club_matrix = tfidf_vectorizer.fit_transform(clubs_df["description_keywords"]) #transforms text in 'description_keywords' into vectors, represents it lexically

    model = SentenceTransformer('all-mpnet-base-v2') #initiaze the Sentence Transformer model
    semantic_club_matrix = model.encode(clubs_df["description_keywords"].tolist()) #transforms text in 'description_keywords' into vectors, represents it semantically
    
    user_input = input("What are you looking for? ")

    print("5. Searching for most relevant matches")
    recommended_clubs = recommend(user_input, club_indices, model, tfidf_vectorizer, semantic_club_matrix, lexical_club_matrix, n=10)

    print("Recommended clubs", recommended_clubs)



if __name__ == "__main__":
    main()