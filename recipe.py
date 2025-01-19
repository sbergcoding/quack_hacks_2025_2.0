
class Recipe:
    def __init__(self, name: str, instructions: str, ingredients={}, location="", servings=1, time=""):
        self.name = name

        # changing instructions to list of steps
        self.instructions = instructions.split("', '")
        self.instructions[0] = self.instructions[0][2:]
        self.instructions.pop()

        self.ingredients = ingredients

        # location is "other" with no location listed
        if location == "" or location == " ":
            self.location = "Other"
        else:
            self.location = location

        self.servings = servings
        self.time = time
    
    def __str__(self):
        string = f"\nName: {self.name}\
            \nLocation: {self.location}\
            \nServings: {self.servings}\
            \nTime: {self.time}\n\
            \nIngredients: "
        
        # formatting ingredients
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