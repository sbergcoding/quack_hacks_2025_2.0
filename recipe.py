
class Recipe:
    def __init__(self, name: str, instructions: str, ingredients={}, location="", servings=1, time="", file_path=""):
        self.name = name

        self.instructions = instructions.split("', '")
        self.instructions[0] = self.instructions[0][2:]
        self.instructions.pop()

        self.ingredients = ingredients

        if location == "" or location == " ":
            self.location = "Other"
        else:
            self.location = location
            
        self.servings = servings
        self.time = time
        self.file_path = file_path

    def add_ingred(self, ingredients: str, amount: str):
        assert ingredients not in self.ingredients, "Ingredient already documented."

        self.ingredients[ingredients] = amount
    
    def __str__(self):
        string = f"\nName: {self.name}\
            \nLocation: {self.location}\
            \nServings: {self.servings}\
            \nTime: {self.time}\n\
            \nIngredients: "
        
        for key in self.ingredients:
            string += f"\n{key} - {self.ingredients[key]}"
        
        # formatting instructions
        string += "\n\nInstructions:"
        for step in self.instructions:
            string += f"\n{step}"

        return string
    
    def __repr__(self):
        string = f"\nName: {self.name}\
            \nLocation: {self.location}\
            \nServings: {self.servings}\
            \nTime: {self.time}\n\
            \nIngredients: "
        
        # formatting ingredients
        for key in self.ingredients:
            string += f"{key} - {self.ingredients[key]}"
        
        # formatting instructions
        string += "\n\nInstructions:"
        for step in self.instructions:
            string += f"\n{step}"

        
        return string