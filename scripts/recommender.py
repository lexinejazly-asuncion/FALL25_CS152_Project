import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def vectorize(clubs_df):
    #concatenates the club caterogy and processed data for each club
    clubs_df["tags"] = (clubs_df["category"].fillna("") + " " +
                        clubs_df["keywords"].fillna("")).str.strip()
    tfidf_vector = TfidfVectorizer() #initialize a vector, where values are the result of td-idf
    tfidf_club_matrix = tfidf_vector.fit_transform(clubs_df["tags"]) #converts data in 'tags' by transforming the text into vectors
    return tfidf_club_matrix

def compute_similarity(tfidf_club_matrix):
    #finds the similarity between the vectors (comparing every club against every club)
    return cosine_similarity(tfidf_club_matrix, tfidf_club_matrix) 

def recommend(clubs_df, club_name, cosine_sim, n):
   indices = pd.Series(clubs_df.index) #creates a series of the club indices
   
   index = indices[indices == club_name].index[0] #the position of the club in the series
   sim_scores = pd.Series(cosine_sim[index]).sort_values(ascending=False) #sorts the similarity scores between the given club and others
   top_hits = list(sim_scores.iloc[1:n+1].index) #takes the top n most similar clubs
   recommended = [list(clubs_df.index)[i] for i in top_hits] #a list of recommended club names
   return recommended
