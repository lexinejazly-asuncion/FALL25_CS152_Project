from bs4 import BeautifulSoup
import json
import requests

from config.paths import GENERATED_CONTENT_CLUB_PATH

#University's website that has all the RSOs on campus
URL = "https://sammyapp.sjsu.edu/club_signup?view=all&c" 

response = requests.get(URL) #returns a response object
soup = BeautifulSoup(response.text, "lxml") #creates a beautifulsoup object that stores the parsed HTML using lxml

rsos = []

def clean_entries(line, prefix = None):
    line = " ".join(line.split())
    if prefix and line.startswith(prefix):
        line = line[len(prefix):]

    return line


def scrape():
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

    # writes the scraped rso informnation into a json file  
    with open(GENERATED_CONTENT_CLUB_PATH, "w", encoding="utf-8") as f:
        json.dump(rsos, f, indent=2, ensure_ascii=False)


