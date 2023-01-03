import requests
from bs4 import BeautifulSoup
import json
import time

# Download the HTML source code for the page
r = requests.get("https://en.wikipedia.org/wiki/List_of_IBA_official_cocktails")

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(r.text, "html.parser")

# Find the main content container
#content = soup.find(id="main")

# Find all of the cocktail cards
cocktail_cards = soup.find_all("dt")

# Create an empty list to store the cocktail dictionaries
cocktails = []

# Iterate over the cocktail cards

for card in cocktail_cards:
    ingredients = []
    metods = []

    name = card.text.strip()
    print(name)
    if name != "Spicy fifty":
        CocktailLink=card.find("a")
        Cr = requests.get("https://en.wikipedia.org" + CocktailLink.attrs["href"])
        CocktailSoup = BeautifulSoup(Cr.text, "html.parser")
        #lista ingredienti non formattata
        Prep_Ingr = CocktailSoup.table.find_all("tr")

        #Filter only ingredients
        
        for ingredienti in Prep_Ingr:
            if "ingredients" in ingredienti.text:
                #ingredients.append(ingrediente.find_all("li"))
                for singolo in ingredienti.find_all("li"):
                # print(singolo)
                    ingredients.append(singolo.text)

        #Filter preparation
        for preparation in Prep_Ingr:
            if "Preparation" in preparation.text:
            #   print(preparation)
                metods.append(preparation.text)

        cocktail = {
            "name": name,
            "ingredients": ingredients,
            "metods": metods
        }
    
    if name == "Spicy fifty":
        cocktail = {
            "name": "Spicy fifty",
            "ingredients": "",
            "metods": "metods"
        }

    cocktails.append(cocktail)
    time.sleep(0.5)

print(len(cocktails))

# Convert the list of cocktails to a JSON string
json_string = json.dumps(cocktails)

# Write the JSON string to a file
with open("cocktailsWiki.json", "w") as f:
    f.write(json_string)

    # Find the ingredients list
