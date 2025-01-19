from recipe import Recipe
import csv

def convert_csv(path: str) -> dict:
    rec_dict = {}

    with open(path, newline='') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=';')

        for row in reader:
            name = row['name']
            instruc = row['instructions']
            ingred = row['ingredients']
            ingred_amount = row['ingredients amount']
            loc = row['location']
            serv = row['servings']
            time = row['time']
            rec_path = row['file_path']

            ingred_li = ingred.split(",")
            amount_li = ingred_amount.split(",")


            ingredients = {}
            for i in range(len(ingred_li)):
                ingredients[ingred_li[i].lower()] = amount_li[i]
            
            recipe = Recipe(name, instruc, ingredients, loc, serv, time, rec_path)
            rec_dict[name] = recipe

    return rec_dict

def main():
    recipes = convert_csv("test.csv")
    print(recipes)

main()