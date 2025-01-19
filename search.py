from recipe import *
from convert import *
def search(input: str, library: list["Recipe"], input_ingredients=[""]) -> list["Recipe"]:
    """Searches using ingredients and a user input. Returns a list of recipes that match the filter"""
    filter_list=[]
    i=0
    if (input!=[""]):
        keys=list(library.keys())
        for i in range(len(keys)):
            if (input in library[keys[i]].name):
                filter_list.append(library[keys[i]])
    if (input_ingredients!=[""]):
        i=0
        temp=[]
        keys=[]
        for i in range(len(filter_list)):
            keys.append(filter_list[i].ingredients.keys())
            for j in range(len(input_ingredients)):
                if (input_ingredients[j] in keys[i]):
                    temp.append(filter_list[i])
        if (len(temp)==len(input_ingredients)):
            return filter_list
        else: 
            #implement AI here
            return ""
    return filter_list 



