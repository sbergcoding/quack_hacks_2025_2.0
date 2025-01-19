from recipe import *
from convert import *
from add_recipe_to_csv import input_to_csv
def search(input_ingredients=[""]) -> list["Recipe"]:
    """Searches using ingredients. Returns a list of recipes that match the filter"""
    filter_list=[]
    for i in range(len(input_ingredients)):
        input_ingredients[i]=input_ingredients[i].lower()
    library=convert_csv("yummy.csv")
    if (input_ingredients!=[""]):
        i=0
        h=0
        for i in range(len(library)):
            keys=list(library[i].ingredients.keys())
            for j in range(len(input_ingredients)):
                for h in range(len(keys)):
                    if (input_ingredients[j] in keys[h]):
                        filter_list.append(library[i])
        if (len(filter_list)>=len(input_ingredients)):
            return filter_list
        else: 
            return None
    return -1
