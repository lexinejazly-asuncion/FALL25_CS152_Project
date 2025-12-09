import os
import json
import requests
from bs4 import BeautifulSoup
from config.paths import CLUB_DATA_JSON
from scripts.model_trainer import make_dir

#University's website that has all the RSOs on campus
URL = "https://sammyapp.sjsu.edu/club_signup?view=all&c" 

response = requests.get(URL) #returns a response object
soup = BeautifulSoup(response.text, "lxml") #creates a beautifulsoup object that stores the parsed HTML using lxml

#for lines that are scraped, removed redundant prefixes
def clean_entries(line, prefix = None):
    line = " ".join(line.split())
    if prefix and line.startswith(prefix):
        line = line[len(prefix):]

    return line

def scrape():

    rsos = []
    #selects all HTML elements with class = 'list-group-item', or the individual rso entries
    for rso in soup.select(".list-group-item"): 
        # scrape the information about the rso
        name_found = rso.select_one(".media-heading.header-cg--h4")
        name = clean_entries(name_found.get_text(strip=True) if name_found else "")
        category_found = rso.select_one("p.h5.media-heading.grey-element")
        category = clean_entries(category_found.get_text(strip=True) if category_found else "")

        # select the mission statement if it exists with class = 'noOutlineOnFocus' and id containing the string 'club_'
        mission_found = rso.select_one("p.noOutlineOnFocus[id*='club_']")
        mission_statement = clean_entries((mission_found.get_text(strip=True) if mission_found else ""), prefix="Mission")

        # select the mission statement if it exists with class = 'noOutlineOnFocus' and id containing the string 'club_whatwedo_'
        benefit_found = rso.select_one("p.noOutlineOnFocus[id*='club_whatwedo_']")
        benefits = clean_entries((benefit_found.get_text(strip=True) if benefit_found else ""), prefix="Membership Benefits")

        rsos.append({
            "name": name,
            "category": category,
            "mission": mission_statement,
            "benefits": benefits

        })

    make_dir(CLUB_DATA_JSON)
    # writes the scraped rso informnation into a json file  
    with open(CLUB_DATA_JSON, "w", encoding="utf-8") as f:
        json.dump(rsos, f, indent=2, ensure_ascii=False)


