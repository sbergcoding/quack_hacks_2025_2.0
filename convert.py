from recipe import Recipe
import csv

def convert_csv(path: str) -> dict:
    rec_dict = {}

    with open(path, newline='') as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            name = row['name']
            instruc = row['instructions']
            ingred = row['ingredients']
            ingred_amount = row['ingredients amount']
            loc = row['location']
            serv = row['servings']
            time = row['time']
            rec_path = row['file_path']

            ingredients = {}
            for i in range(len(ingred)):
                ingredients[ingred[i]] = ingred_amount[i]
            
            recipe = Recipe(name, instruc, ingredients, loc, serv, time, rec_path)
            rec_dict[name] = recipe

    return rec_dict

def main():
    recipes = convert_csv("test.csv")
    print(recipes)

main()