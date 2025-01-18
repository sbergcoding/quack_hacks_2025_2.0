
class Recipe:
    def __init__(self, name: str, instruc: str, ingreds={}, location="", servings="", time="", file_path=""):
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
    
