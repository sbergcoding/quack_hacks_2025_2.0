from recipe import *
from convert import *
from add_recipe_to_csv import input_to_csv
def search(library: dict["Recipe"], input_ingredients=[""]) -> list["Recipe"]:
    """Searches using ingredients and a user input. Returns a list of recipes that match the filter"""
    filter_list=[]
    if (input_ingredients!=[""]):
        i=0
        keys=list(library.keys())
        for i in range(len(keys)):
            keys2=(list(library[keys[i]].ingredients.keys()))
            for j in range(len(input_ingredients)):
                if (input_ingredients[j] in keys2):
                    filter_list.append(library[keys[i]])

        if (len(filter_list)==len(input_ingredients)):
            return filter_list
        else: 
            return None
    return -1
library=convert_csv("test.csv") 
print(search(library, ["bread", "cheese"]))



