def small_shop(product, sity, quantity):

    price = 0

    if sity == "Sofia":
        if product == "coffee":
            price = 0.5
        elif product == "water":
            price = 0.8
        elif product == "beer":
            price = 1.2
        elif product == "sweets":
            price = 1.45
        elif product == "peanuts":
            price = 1.6

    elif sity == "Plovdiv":
        if product == "coffee":
            price = 0.4
        elif product == "water":
            price = 0.7
        elif product == "beer":
            price = 1.15
        elif product == "sweets":
            price = 1.3
        elif product == "peanuts":
            price = 1.5

    elif sity == "Varna":
        if product == "coffee":
            price = 0.45
        elif product == "water":
            price = 0.7
        elif product == "beer":
            price = 1.1
        elif product == "sweets":
            price = 1.35
        elif product == "peanuts":
            price = 1.55

    total_price = price * quantity
    return f"{total_price:.2f}"


product = input()
town = input()
quantity = float(input())
print(small_shop(product, town, quantity))
