ROSE_PRICE = 5
DAHLIA_PRICE = 3.8
TULIP_PRICE = 2.8
NARCIS_PRICE = 3
GLADIOLA_PRICE = 2.5


def new_house(flowers, count, budget):
    price = 0
    if flowers == "Roses":
        price = ROSE_PRICE * count
        if count > 80:
            price *= 0.9
    elif flowers == "Dahlias":
        price = DAHLIA_PRICE * count
        if count > 90:
            price *= 0.85
    elif flowers == "Tulips":
        price = TULIP_PRICE * count
        if count > 80:
            price *= 0.85
    elif flowers == "Narcissus":
        price = NARCIS_PRICE * count
        if count < 120:
            price *= 1.15
    elif flowers == "Gladiolus":
        price = GLADIOLA_PRICE * count
        if count < 80:
            price *= 1.2

    if price <= budget:
        return f"Hey, you have a great garden with {count} {flowers} " \
               f"and {budget-price:.2f} leva left."
    return f"Not enough money, you need {price-budget:.2f} leva more."


flowers_kind = input()
flowers_count = int(input())
budget = float(input())
result = new_house(flowers_kind, flowers_count, budget)
print(result)
