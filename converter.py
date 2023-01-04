import requests
from bs4 import BeautifulSoup
import json
import time

# Download the HTML source code for the page
r = requests.get("https://iba-world.com/category/iba-cocktails/")

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(r.text, "html.parser")

# Find the main content container
#content = soup.find(id="main")

# Find all of the cocktail cards
cocktail_cards = soup.find_all("article")

# Create an empty list to store the cocktail dictionaries
cocktails = []

# Iterate over the cocktail cards

for card in cocktail_cards:
    ingredients = []

    CocktailLink=card.find("h3").find('a')

    name=CocktailLink.text.strip()
    print(name)

    Cr = requests.get(CocktailLink.attrs["href"])
    CocktailSoup = BeautifulSoup(Cr.text, "html.parser")
    #lista ingredienti non formattata
    Prep_Ingr = CocktailSoup.table.find_all("h3")
    
    #Filter only ingredients
    
    for ingredienti in Prep_Ingr:
        if "ingredients" in ingredienti.text:
            for singolo in ingredienti.find_all("li"):
                singolo = singolo.text
                ingredients.append(singolo)

    #Filter preparation
    for preparation in Prep_Ingr:
        if "Preparation" in preparation.text:
            metods = preparation.text.replace("Preparation","")

    cocktail = {
        "name": name,
        "ingredients": ingredients,
        "metods": metods,
        "note": note,
        "garnish": garnish
    }
    cocktails.append(cocktail)
    break
    time.sleep(10.0)
    
#print(len(cocktails))

# Convert the list of cocktails to a JSON string
json_string = json.dumps(cocktails)

# Write the JSON string to a file
with open("cocktailsWiki.json", "w") as f:
    f.write(json_string)

    # Find the ingredients list
