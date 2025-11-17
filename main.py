from scripts.scrape_web import scrape
from scripts.load_and_process_data import load_clubs, json_to_dframe, preprocess
from scripts.recommender import vectorize, compute_similarity, recommend
from config.paths import GENERATED_CONTENT_CLUB_PATH

def main():
    scrape() #scrape the website
    clubs = load_clubs(GENERATED_CONTENT_CLUB_PATH) #load the data scraped about clubs
    clubs_df = json_to_dframe(clubs) #create a dframe from the loaded data
    print(clubs_df.head(10))

    print()

    clubs_df["keywords"] = clubs_df["mission_and_benefits"].apply(preprocess)
    clubs_df = clubs_df[["category", "keywords"]] 
    print(clubs_df.head(10))

    tdidf_clubs = vectorize(clubs_df)
    cosine_sim = compute_similarity(tdidf_clubs)

    example_club = clubs_df.index[10]  # just pick the first club
    recommendations = recommend(clubs_df, example_club, cosine_sim, 15)

    print(f"\nTop recommendations for '{example_club}':")
    print(recommendations)



if __name__ == "__main__":
    main()