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

def list_to_instructions(instructions):
    for i in range(len(instructions)):
        instructions[i] = str(i+1) + ". " + instructions[i].get()
    return ", ".join(instructions)

def list_to_ingredients(ingredients):
    temp = []
    for item in ingredients:
        temp.append(item[0].get())
    return ",".join(temp)

def list_to_amounts(ingredients):
    temp = []
    for item in ingredients:
        temp.append(item[1].get())
    return "', '".join(temp)

# This function takes in the name of the recipe, instructions, ingredients, ingredients_amount, location, servings, time and writes it to the yummy.csv file.
def input_to_csv(name,  ingredients, ingredients_amount, instructions, servings, time):
    with open("yummy.csv", "a") as f:
        f.write(f"{name};{ingredients};{ingredients_amount};{instructions};;{servings};{time};\n")