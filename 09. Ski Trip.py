ROOM_FOR_ONE_PERSON = 18
APARTMENT = 25
PRESIDENT_APARTMENT = 35


def ski_trip(days, room_type, evaluation):

    total_nights = days - 1
    price = 0

    if room_type == "room for one person":
        price = total_nights * ROOM_FOR_ONE_PERSON

    elif room_type == "apartment":
        if total_nights < 10:
            price = (total_nights * APARTMENT) * 0.7
        elif 10 <= total_nights <= 15:
            price = (total_nights * APARTMENT) * 0.65
        elif total_nights > 15:
            price = (total_nights * APARTMENT) * 0.5

    elif room_type == "president apartment":
        if total_nights < 10:
            price = (total_nights * PRESIDENT_APARTMENT) * 0.9
        elif 10 <= total_nights <= 15:
            price = (total_nights * PRESIDENT_APARTMENT) * 0.85
        elif total_nights > 15:
            price = (total_nights * PRESIDENT_APARTMENT) * 0.8

    if evaluation == "positive":
        price *= 1.25
    else:
        price *= 0.9

    return f"{price:.2f}"


days = int(input())
room_type = input()
evaluation = input()
result = ski_trip(days, room_type, evaluation)
print(result)
