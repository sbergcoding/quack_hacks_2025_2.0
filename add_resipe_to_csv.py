import app

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
