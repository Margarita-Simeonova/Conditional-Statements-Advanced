def fruit_or_vegetable(product):

    if product == "banana" or product == "apple" or product == "kiwi" or product == "cherry" or product == "lemon" or product == "grapes":
        return "fruit"
    elif product == "tomato" or product == "cucumber" or product == "pepper" or product == "carrot":
        return "vegetable"
    else:
        return "unknown"


product = input()
print(fruit_or_vegetable(product))
