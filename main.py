from scripts.scrape_web import scrape
from scripts.load_and_process_data import load_clubs, json_to_dframe, preprocess
from config.paths import GENERATED_CONTENT_CLUB_PATH

def main():
    scrape() #scrape the website
    clubs = load_clubs(GENERATED_CONTENT_CLUB_PATH) #load the data scraped about clubs
    clubs_df = json_to_dframe(clubs) #create a dframe from the loaded data
    print(clubs_df.head(10))

    clubs_df["tags_processed"]= clubs_df["tags"].apply(preprocess)
    clubs_df = clubs_df[["category", "tags_processed"]] 
    print(clubs_df.head(10))


if __name__ == "__main__":
    main()