def animal_type(animal):

    if animal == "dog":
        return "mammal"
    elif animal == "crocodile" or animal == "tortoise" or animal == "snake":
        return "reptile"

    else:
        return "unknown"


animal = input()
print(animal_type(animal))
