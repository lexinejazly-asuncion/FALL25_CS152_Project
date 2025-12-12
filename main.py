import os

from Model.scripts.model_trainer import train_and_initialize_models
from Model.scripts.scrape_web import scrape
from Model.scripts.load import load_clubs, json_to_dframe
from Model.scripts.process import preprocess
from config.paths import CLUB_DATA_JSON, LEXICAL_MATRIX_PATH, SEMANTIC_MATRIX_PATH, CLUB_INDICES_PATH

#Intializes the data and models if they don't already exist, other wise, loads them from the saved generated_content path
#before running the app.py web application, MAIN.PY MUST BE RAN ONCE SO DATA, MODELS, AND EMBEDDINGS ARE INITIALIZED
def main():
    print("Searching for trained models and data...\n")
    #check if club data and models have already been initialized, at least one of them does not, re-initialize them
    if not os.path.exists(CLUB_DATA_JSON) or not os.path.exists(LEXICAL_MATRIX_PATH) or not os.path.exists(SEMANTIC_MATRIX_PATH) or not os.path.exists(CLUB_INDICES_PATH):
        print("Necessary models and data cannot be found. Initializing data and creating vector embeddings...\n")
        
        scrape() #call scrape method to get information about clubs
        print("Finished: Scraping university website for club data from descriptions\n")

        clubs = load_clubs(CLUB_DATA_JSON) #load the data scraped about clubs
        clubs_df = json_to_dframe(clubs) #create a dframe from the loaded data
        print("Finished: Loading the club data\n")

        clubs_df["description_keywords"] = clubs_df["description"].apply(preprocess) #takes only important words from name, category, mission, and benefits
        print("Finished: Processing the club data\n")
        
        print("Calculating and initializing vector embeddings\n")
        train_and_initialize_models(clubs_df)

        print("Intialized the necessary models and data. You may now run app.py to access the FindYourRSO web application.\n ")

    else:
        print("Found necessary models and data. You may now run app.py to access the FindYourRSO web application.\n")

    
    
if __name__ == "__main__":
    main()