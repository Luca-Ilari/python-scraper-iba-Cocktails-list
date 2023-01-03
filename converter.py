import requests
from bs4 import BeautifulSoup
import json

# Download the HTML source code for the page
r = requests.get("https://it.wikipedia.org/wiki/Cocktail_ufficiali_IBA")

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(r.text, "html.parser")

# Find the main content container
#content = soup.find(id="main")

# Find all of the cocktail cards
cocktail_cards = soup.find_all("li")

# Create an empty list to store the cocktail dictionaries
cocktails = []

# Iterate over the cocktail cards

for card in cocktail_cards:
    name = card.find("h3").text.strip()
    print(name)

    CocktailLink=card.find("a")
    Cr = requests.get(CocktailLink.attrs["href"])
    CocktailSoup = BeautifulSoup(Cr.text, "html.parser")


################
    if "INGREDIENTS" in card.text:
        desc = card.text.strip()
        desc = desc.split("\n")

    ingredients = []
    cocktail = {
        "name": name,
        "ingredients": ingredients,
        "metods": metods
    }
    cocktails.append(cocktail)

# Convert the list of cocktails to a JSON string
json_string = json.dumps(cocktails)

# Write the JSON string to a file
with open("cocktailsWiki.json", "w") as f:
    f.write(json_string)

    # Find the ingredients list
