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
    df["description"] = (df["name"] + " " + df["category"] + " " + df["mission"] + " " + df["benefits"]).str.strip()
    
    #create a temporary column for the length of the description
    df['description_length'] = df['description'].str.len()

    #sort the dframe by name (to group duplicates) and then by length (descending) to make sure the longest description for any given name is at the top of its group
    df = df.sort_values(by=['name', 'description_length'], ascending=[True, False])

    #drop duplicates, keeping only one entry per club, taking which description is longer
    df = df.drop_duplicates(subset=['name'], keep='first')
    
    #drop the temporary length column
    df = df.drop(columns=['description_length'])

    df = df[["name","description"]] #selects columns 'name' and 'tags'

    df = df.set_index("name") #set the name of club as the index

    return df
