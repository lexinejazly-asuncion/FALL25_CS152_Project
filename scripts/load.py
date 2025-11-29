import pandas as pd
import json

#loads the club data from the json file
def load_clubs(CLUB_PATH):
    with open(CLUB_PATH, "r", encoding = "utf-8") as f:
        clubs = json.load(f)

    return clubs

#initializes a dataframe from the loaded club data
def json_to_dframe(clubs):
    df = pd.DataFrame(clubs)

    #create a new column 'tags' that concatenates the data from 'mission' and 'benefits'
    df["description"] = (df["category"] + " " + df["mission"] + " " + df["benefits"]).str.strip()
    
    df = df[["name","description"]] #selects columns 'name' and 'tags'

    df = df.set_index("name") #set the name of club as the index

    return df
