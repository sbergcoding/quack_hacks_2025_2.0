from openai import OpenAI
# Read API key from a file
openai_key = open("API_KEY", "r").read()
OpenAI.api_key = openai_key
client = OpenAI(api_key= openai_key)
# calls the OpenAI API to generate a recipe
def generate_recipe(ingredients):
    # Create a prompt for the AI
    prompt =  f"Create a recipe using the following ingredients: {', '.join(ingredients)}. Please provide the recipe with the following sections:\n" \
             "Recipe Name:  line Recipe Name t\n" \
             "Ingredients List:  line Ingredients List \n" \
             "Ingredients Amount: line Ingredients Amount\n" \
             "Numbered Step-by-Step Instructions: numbered Step-by-step Instructions\n" \
             "Total Time: Total Time in just one number\n" \
             "Location: Where the recipe is from (e.g., country or region)just give a country\n" \
             "Number of Servings: Number of Servings \n" \
             "Ensure the recipe is easy to follow, clear, and well-organized."
    
    # Call the OpenAI API
    try:
        response = client.chat.completions.create(
    model="gpt-4o-mini-2024-07-18",  # Correct model name
    messages=[
        {"role": "system", "content": "You are a helpful assistant specialized in creating recipes."},
        {"role": "user", "content": prompt}
    ],
    response_format={
        "type": "json_schema", 
        "json_schema": {
            "name": "Recipe",
            "schema": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "The name of the recipe"
                    },
                    "instructions": {
                        "type": "string",
                        "description": "The step-by-step instructions for the recipe, with each step separated by a period and space."
                    },
                    "ingredients": {
                        "type": "string",
                        "description": "A comma-separated list of ingredients. with no amounts or measurements."
                    },
                    "ingredients_amount": {
                        "type": "string",
                        "description": "A comma-separated list of ingredient amounts corresponding to the ingredients list."
                    },
                    "location": {
                        "type": "string",
                        "description": "The country or region where the recipe is from."
                    },
                    "servings": {
                        "type": "integer",
                        "description": "The number of servings the recipe makes."
                    },
                    "time": {
                        "type": "string",
                        "description": "The total time required to make the recipe."
                    }
                },
                "required": [
                    "name", 
                    "instructions", 
                    "ingredients", 
                    "ingredients_amount", 
                    "location", 
                    "servings", 
                    "time"
                ],
                "additionalProperties": False
            }
        }
    }
)


        # Extract the text from the response
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"

# Test the function
def reformat_recipe(recipe_json):
    """
    Reformat a recipe JSON string into the specified custom format.
    
    Parameters:
        recipe_json (str): A JSON string containing the recipe data.
        
    Returns:
        str: The reformatted recipe string.
    """
    import json
    
    # Parse the JSON string into a Python dictionary
    recipe = json.loads(recipe_json)
    
    # Extract the recipe components
    name = recipe.get("name", "Unknown Recipe")
    ingredients = recipe.get("ingredients", "").replace(", ", ",")
    ingredients_amount = recipe.get("ingredients_amount", "").replace(", ", ",")
    instructions = recipe.get("instructions", "").replace(". ", ". ").replace(". ", " ")
    location = recipe.get("location", "Unknown Location")
    servings = str(recipe.get("servings", "Unknown Servings"))
    time = recipe.get("time", "Unknown Time")
    
    # Construct the reformatted string
    reformatted_recipe = (
        f"{name};"
        f"{ingredients};"
        f"{ingredients_amount};"
        f"{instructions};"
        f"{location};"
        f"{servings};"
        f"{time}"
    )
    
    return reformatted_recipe

