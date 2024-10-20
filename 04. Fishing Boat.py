SPRING_PRICE = 3000
SUMMER_AND_AUTUMN_PRICE = 4200
WINTER_PRICE = 2600


def fishing_boat(budget, season, peoples_count):

    price = 0

    if season == "Spring":
        price = SPRING_PRICE
    elif season == "Summer" or season == "Autumn":
        price = SUMMER_AND_AUTUMN_PRICE
    elif season == "Winter":
        price = WINTER_PRICE

    if peoples_count <= 6:
        price *= 0.9
    elif 6 < peoples_count <= 11:
        price *= 0.85
    elif peoples_count > 11:
        price *= 0.75

    if peoples_count % 2 == 0 and not season == "Autumn":
        price *= 0.95

    if price <= budget:
        return f"Yes! You have {budget-price:.2f} leva left."
    return f"Not enough money! You need {price-budget:.2f} leva."


budget = float(input())
season = input()
peoples_count = int(input())
result = fishing_boat(budget, season, peoples_count)
print(result)
