def invalid():
    print("Invalid input, please try again")


def ingredientsList():
    ingredientItem = input("Ingredients: ")
    ingredientList = ingredientItem.split(", ")
    items = 0
    print(ingredientList)

    """
    for i in range(ingredientItem):
        if i == ",":
            #delete
            list.pop(i)

    for i in range(len(list)):
        items += 1
        """
ingredientsList()
