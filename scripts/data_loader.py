import pandas as pd
import os
import json

def load_clubs(CLUB_PATH):
    print(f"Loading clubs: ")
    with open(CLUB_PATH, "r", encoding = "utf-8") as f:
        clubs = json.load(f)

    return clubs

def json_to_dframe(clubs):
    df = pd.DataFrame(clubs)

    df["tags"] = (df["name"] + " " + df["category"] + " " + df["mission"] + " " + df["benefits"]).str.strip()
    
    return df

