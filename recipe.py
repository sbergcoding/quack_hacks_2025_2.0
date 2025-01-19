
class Recipe:
    def __init__(self, name: str, instruc: str, ingreds={}, location="", servings=1, time="", file_path=""):
        self.name = name
        self.instruc = instruc
        self.ingreds = ingreds
        self.location = location
        self.servings = servings
        self.time = time
        self.file_path = file_path

    def add_ingred(self, ingred: str, amount: str):
        assert ingred not in self.ingreds, "Ingredient already documented."

        self.ingreds[ingred] = amount
    
    def __str__(self):
        return f"\nName: {self.name}\nInstructions: {self.instruc}\nIngredients: {self.ingreds}\n"
    
    def __repr__(self):
        return f"\nName: {self.name}\nInstructions: {self.instruc}\nIngredients: {self.ingreds}\n"


def main():
    test = Recipe("Grilled Cheese", "Don't burn", {"cheese": "2 slices", "bread": "2 slices"}, time="2 minutes")
    
main()
