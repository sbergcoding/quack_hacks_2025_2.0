import openai
# Read API key from a file
API_key = open("API_KEY", "r").read().strip()
openai.api_key = API_key
# calls the OpenAI API to generate a recipe
def generate_recipe(ingredients):
    # Create a prompt for the AI
    prompt =  f"Create a recipe using the following ingredients: {', '.join(ingredients)}. Please provide the recipe with the following sections:\n" \
             "Recipe Name: on a new line Recipe Name given first\n" \
             "Ingredients List: on a new line Ingredients List (with measurements) given third\n" \
             "Numbered Step-by-Step Instructions: on a new line numbered Step-by-step Instructions given second\n" \
             "Total Time: on a new line Total Time given last in just one number\n" \
             "Location: on a new line Where the recipe is from (e.g., country or region) given fourth  just give a country\n" \
             "Number of Servings: on a new line Number of Servings given fifth\n" \
             "Ensure the recipe is easy to follow, clear, and well-organized."
    
    # Call the OpenAI API
    try:
        response = openai.chat.completions.create(
            model="gpt-4",  # Correct model name
            messages=[
                {"role": "system", "content": "You are a helpful assistant specialized in creating recipes."},
                {"role": "user", "content": prompt}
            ]
        )
        # Extract the text from the response
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"

# Test the function
print(generate_recipe(["cheese", "chocolate", "gummy bears", "chicken"]))


