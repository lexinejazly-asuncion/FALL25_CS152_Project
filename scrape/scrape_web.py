import requests

from bs4 import BeautifulSoup

import json

#University's website that has all the RSOs on campus
URL = "https://sammyapp.sjsu.edu/club_signup?view=all&c" 

response = requests.get(URL) #returns a response object
soup = BeautifulSoup(response.text, "lxml") #creates a beautifulsoup object that stores the parsed HTML using lxml

rsos = []

def scrape_web():
    #selects all HTML elements with class = 'list-group-item', or the individual rso entries
    for rso in soup.select(".list-group-item"): 
        # scrape the information about the rso
        name_found = rso.select_one(".media-heading.header-cg--h4")
        name = name_found.get_text(strip=True) if name_found else ""
        category_found = rso.select_one("p.h5.media-heading.grey-element")
        category = category_found.get_text(strip=True) if category_found else ""

        # select the mission statement if it exists with class = 'noOutlineOnFocus' and id containing the string 'club_'
        mission_found = rso.select_one("p.noOutlineOnFocus[id*='club_']")
        mission_statement = mission_found.get_text(strip=True) if mission_found else ""

        # select the mission statement if it exists with class = 'noOutlineOnFocus' and id containing the string 'club_whatwedo_'
        benefit_found = rso.select_one("p.noOutlineOnFocus[id*='club_whatwedo_']")
        benefits = benefit_found.get_text(strip=True) if benefit_found else ""

        rsos.append({
            "name": name,
            "category": category,
            "mission": mission_statement,
            "benefits": benefits

        })

    # writes the scraped rso informnation into a json file  
    with open("rso.json", "w", encoding="utf-8") as f:
        json.dump(rsos, f, indent=2)

if __name__ == "__main__":
    scrape_web()



