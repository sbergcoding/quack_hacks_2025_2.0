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
    with open("test.csv", "a") as f:
        f.write(f"\n{name};{instructions};{ingredients};{ingredients_amount};{location};{servings};{time}; None") 

def main():
    name = "grilled cheese"
    instructions = ["1. make sandwich", "2. grill sandwich"]
    ingredients_dict = {"bread": "2 slices", "cheese": "2 slices"}
    location = "american"
    servings = 1
    time = "30 mins"
    
    ingredients = ingredient_keys_to_str(ingredients_dict)
    ingredients_amount = ingredient_values_to_str(ingredients_dict)

    input_to_csv(name, instructions, ingredients, ingredients_amount, location, servings, time)

main()