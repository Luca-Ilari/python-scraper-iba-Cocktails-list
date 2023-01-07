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
    note="N/A"
    garnish="N/A"
    time.sleep(2.0)
    CocktailLink=card.find("h3").find('a')

    name=CocktailLink.text.strip()
    print(name)

    Cr = requests.get(CocktailLink.attrs["href"])
    CocktailSoup = BeautifulSoup(Cr.text, "html.parser")
    #lista ingredienti non formattata
    Prep_Ingr = CocktailSoup.find_all("div", {"class": "et_pb_module et_pb_post_content et_pb_post_content_0_tb_body blog-post-content"})
    Singoli_p = Prep_Ingr[0].find_all("p")
    i=0
    for par in (Singoli_p):
        if i == 0:
            #Ingredients
            for line in par:
                if line.text: #remove </br> from <p>
                    unit="N/A"
                    ammount="N/A"
                    if "ml" in line:
                        unit = "ml"
                    else:
                        unit= ""
                    if line.split("ml")[0]:
                       ammount = line.text.split("ml")[0]
                       spirit = line.split("ml")[1]
                    else:
                        spirit=line.strip
                    Single={
                    "unit": unit.strip(),
                    "amount": ammount.strip(),
                    "ingredient": spirit.strip(),
                    }
                    ingredients.append(Single)
            
        if i == 1:
            #metods
            methods = par.text
        if i == 2:
            #garnish
            garnish = par.text
        if i == 3:
            #note
            note = par.text
        i=i+1

    cocktail = {
        "name": name,
        "ingredients": ingredients,
        "methods": methods,
        "garnish": garnish,
        "note": note
    }
    cocktails.append(cocktail)
    print (cocktails)
    time.sleep(60.0)

    
#print(len(cocktails))

# Convert the list of cocktails to a JSON string
json_string = json.dumps(cocktails)

# Write the JSON string to a file
with open("cocktailsWiki.json", "w") as f:
    f.write(json_string)

    # Find the ingredients list
