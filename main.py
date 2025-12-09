import os

from scripts.model_trainer import train_and_initialize_models
from scripts.scrape_web import scrape
from scripts.load import load_clubs, json_to_dframe
from scripts.process import preprocess
from scripts.recommender import find_similar_clubs, recommend
from config.paths import CLUB_DATA_JSON, LEXICAL_MATRIX_PATH, SEMANTIC_MATRIX_PATH

def main():
    #check if club data and models have already been initialized, if so load them
    if os.path.exists(CLUB_DATA_JSON) and os.path.exists(LEXICAL_MATRIX_PATH) and os.path.exists(SEMANTIC_MATRIX_PATH):
        clubs = load_clubs(CLUB_DATA_JSON) #load the data scraped about clubs
        clubs_df = json_to_dframe(clubs) #create a dframe from the loaded data
        club_indices = clubs_df.index.tolist()
    
    #otherwise initialize them
    else:
        scrape() #call scrape method to get information about clubs

        clubs = load_clubs(CLUB_DATA_JSON) #load the data scraped about clubs
        clubs_df = json_to_dframe(clubs) #create a dframe from the loaded data

        clubs_df["description_keywords"] = clubs_df["description"].apply(preprocess) #takes only important words from name, category, mission, and benefits
        club_indices = clubs_df.index.tolist()

        train_and_initialize_models(clubs_df)
    
    #ask for user query   
    #user_input = input("What are you looking for? ")
    user_input = "I am interested in clubs that combine electrical engineering and computer science research"

    recommended_clubs = recommend(user_input, club_indices, n=20)

    print("Recommended clubs", recommended_clubs)

    # !!!!!! TO IMPLEMENT LATER: find_similar_clubs(selected_club_names, club_indices, n=10) !!!!

if __name__ == "__main__":
    main()