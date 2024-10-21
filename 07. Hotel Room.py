def hotel_room(month, nights_count):

    studio_price = 0
    apartment_price = 0

    if month == "May" or month == "October":
        studio_price = 50 * nights_count
        apartment_price = 65 * nights_count
        if nights_count > 14:
            studio_price *= 0.7
        elif nights_count > 7:
            studio_price *= 0.95

    elif month == "June" or month == "September":
        studio_price = 75.2 * nights_count
        apartment_price = 68.7 * nights_count
        if nights_count > 14:
            studio_price *= 0.8

    elif month == "July" or month == "August":
        studio_price = 76 * nights_count
        apartment_price = 77 * nights_count

    if nights_count > 14:
        apartment_price *= 0.9

    return f"Apartment: {apartment_price:.2f} lv.\nStudio: {studio_price:.2f} lv."


month = input()
nights = int(input())
result = hotel_room(month, nights)
print(result)
