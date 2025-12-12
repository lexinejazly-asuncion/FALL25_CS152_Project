import os

from Model.scripts.model_trainer import train_and_initialize_models
from Model.scripts.scrape_web import scrape
from Model.scripts.load import load_clubs, json_to_dframe
from Model.scripts.process import preprocess
from Model.scripts.recommender import load_recommendation_models, recommend
from config.paths import CLUB_DATA_JSON, LEXICAL_MATRIX_PATH, SEMANTIC_MATRIX_PATH, CLUB_INDICES_PATH

def main():
    #check if club data and models have already been initialized, if not initialize them
    if not os.path.exists(CLUB_DATA_JSON) and not os.path.exists(LEXICAL_MATRIX_PATH) and not os.path.exists(SEMANTIC_MATRIX_PATH) and not os.path.exists(CLUB_INDICES_PATH):
        scrape() #call scrape method to get information about clubs

        clubs = load_clubs(CLUB_DATA_JSON) #load the data scraped about clubs
        clubs_df = json_to_dframe(clubs) #create a dframe from the loaded data

        clubs_df["description_keywords"] = clubs_df["description"].apply(preprocess) #takes only important words from name, category, mission, and benefits

        train_and_initialize_models(clubs_df)

        loaded_models = load_recommendation_models()
    else:
        #load all models and matrices
        loaded_models = load_recommendation_models()
    
    #ask for user query   
    #user_input = input("What are you looking for? ")
    user_input = "I want to join a club for business majors. I would like to have chances to " \
    "network with professionals and also connect with alumni. If there is a possibility, " \
    "I would also like to work on consulting projects."

    recommended_clubs = recommend(user_input, loaded_models, n=20)
    print("Recommended clubs", recommended_clubs)

if __name__ == "__main__":
    main()