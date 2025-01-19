import openai
import app
# Read API key from a file
API_key = open("API_KEY", "r").read().strip()
openai.api_key = API_key

def generate_recipe(ingredients):
    # Create a prompt for the AI
    prompt = f"Create a recipe using the following ingredients: {', '.join(ingredients)}. Provide a step-by-step guide with measurements and cooking instructions."
    
    # Call the OpenAI ChatCompletion API
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


