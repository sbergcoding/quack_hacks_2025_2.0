import app

# This function loops through the ingredients and if the first letter is uppercase, it adds the ingredient to the list with the ingredient in lowercase. If the first letter is lowercase, it adds the ingredient to the list with the ingredient in uppercase.
def format_ingredients(ingredients):
    for i in range(len(ingredients)):
        if i[0].isupper():
            ingredients[i] = ingredients[i]+"|"+ingredients[i].lower()
        else:
            ingredients[i] = ingredients[i].capitalize()+"|"+ingredients[i]


# This function takes in the name of the recipe, instructions, ingredients, ingredients_amount, location, servings, time and writes it to the yummy.csv file.
def ingredient_keys_to_str(ingredients):
    return "["+ ",".join(ingredients.keys())+"]"

# This function takes in the ingredients and returns the keys of the ingredients dictionary as a string.
def ingredient_values_to_str(ingredients):
    return "["+",".join(ingredients.values())+"]"

def instructions_to_str(instructions):
    return "\n".join([f"{i+1}. {instruction}" for i, instruction in enumerate(instructions)]) + "\n\n"
        

# This function takes in the name of the recipe, instructions, ingredients, ingredients_amount, location, servings, time and writes it to the yummy.csv file.
def input_to_csv(name, instructions, ingredients, ingredients_amount, location, servings, time):
    with open("yummy.csv", "a") as f:
        f.write(f"{name};{instructions};{ingredients};{ingredients_amount};{location};{servings};{time};\n") 

def main():
    name = app.name
    instructions = app.instructions
    ingredients_dict = app.ingredient_dict
    location = app.location
    servings = app.servings
    time = app.time
    
    ingredients = ingredient_keys_to_str(ingredients_dict)
    ingredients_amount = ingredient_values_to_str(ingredients_dict)
    formated_ingredients = format_ingredients(ingredients)

    input_to_csv(name, instructions, formated_ingredients, ingredients_amount, location, servings, time)
