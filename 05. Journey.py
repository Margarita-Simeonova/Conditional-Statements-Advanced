def journey(budget, season):

    price = 0
    destination = ""
    place = ""

    if season == "summer":
        if budget <= 100:
            destination = "Bulgaria"
            place = "Camp"
            price = budget * 0.3
        elif 100 < budget <= 1000:
            destination = "Balkans"
            place = "Camp"
            price = budget * 0.4
        elif budget > 1000:
            destination = "Europe"
            place = "Hotel"
            price = budget * 0.9

    elif season == "winter":
        if budget <= 100:
            destination = "Bulgaria"
            place = "Hotel"
            price = budget * 0.7
        elif 100 < budget <= 1000:
            destination = "Balkans"
            place = "Hotel"
            price = budget * 0.8
        elif budget > 1000:
            destination = "Europe"
            place = "Hotel"
            price = budget * 0.9

    return f"Somewhere in {destination}\n{place} - {price:.2f}"


budget = float(input())
season = input()
result = journey(budget, season)
print(result)
