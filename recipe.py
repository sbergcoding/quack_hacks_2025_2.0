
class Recipe:
    def __init__(self, name: str, instructions: str, ingredients={}, location="", servings=1, time="", file_path=""):
        self.name = name
        self.instructions = instructions
        self.ingredients = ingredients
        self.location = location
        self.servings = servings
        self.time = time
        self.file_path = file_path

    def add_ingred(self, ingredients: str, amount: str):
        assert ingredients not in self.ingredients, "Ingredient already documented."

        self.ingredients[ingredients] = amount
    
    def __str__(self):
        return f"\nName: {self.name}\nInstructions: {self.instructions}\nIngredients: {self.ingredients}\n"
    
    def __repr__(self):
        return f"\nName: {self.name}\nInstructions: {self.instructions}\nIngredients: {self.ingredients}\n"