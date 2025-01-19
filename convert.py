from recipe import Recipe
import csv

def convert_csv(path: str) -> dict:
    rec_list = []

    with open(path, newline='', encoding='utf8') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=";")

        for row in reader:
            name = row['name']
            ingred = row['ingredients']
            ingred_amount = row['ingredients_amount']
            instruc = row['instructions']
            loc = row['location']
            serv = row['servings']
            time = row['time']

            ingred_li = ingred.split(",")
            amount_li = ingred_amount.split(",")


            ingredients = {}
            for i in range(len(ingred_li)):
                ingredients[ingred_li[i].lower()] = amount_li[i]
            
            
            recipe = Recipe(name, instruc, ingredients, loc, serv, time)
            rec_list.append(recipe)

    return rec_list
