library = {
    "sweet": ["chocolate"],
    "fruit": ["strawberry"],
    "protein": ["meat", "chicken"],
    "drink": ["water"]
}

def main():
    print("Testing the output for specific recipes...")
    while True:
        try:
            ingredients_list = get_ingredients()
            matching_recipes = find_matching_recipes(library, ingredients_list)
            if matching_recipes:
                print(f"Matching recipes: {', '.join(matching_recipes)}")
                print(matching_recipes)
            else:
                print("No matching recipes found.")
            break  # Exit the loop after successful input
        except ValueError as e:
            print(e)

def get_ingredients():
    # Prompts the user for ingredients and returns them as a list
    ingredient_input = input("Enter ingredients: ").strip()
    if not ingredient_input:
        raise ValueError("Invalid input, please provide at least one ingredient.")
    return [item.strip() for item in ingredient_input.split(",")]

def find_matching_recipes(library, ingredients):
    # Finds the matching recipes based on the user's ingredients
    # Flatten the library values into a single list
    all_ingredients = [item for sublist in library.values() for item in sublist]
    return [ingredient for ingredient in ingredients if ingredient in all_ingredients]

# hlkeeecwqvvqwe beqrb erq re rwe erdat fsg gsnfgnwrfhwrnera

if __name__ == "__main__":
    main()
