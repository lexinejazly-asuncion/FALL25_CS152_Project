from scripts.scrape_web import scrape
from scripts.data_loader import load_clubs, json_to_dframe
from config.paths import GENERATED_CONTENT_CLUB_PATH

def main():
    scrape()
    clubs = load_clubs(GENERATED_CONTENT_CLUB_PATH)
    clubs_df = json_to_dframe(clubs)
    print(clubs_df.head(10))


if __name__ == "__main__":
    main()