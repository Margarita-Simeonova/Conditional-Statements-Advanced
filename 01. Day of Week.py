def day_of_week(numb):

    if numb == 1:
        return "Monday"
    elif numb == 2:
        return "Tuesday"
    elif numb == 3:
        return "Wednesday"
    elif numb == 4:
        return "Thursday"
    elif numb == 5:
        return "Friday"
    elif numb == 6:
        return "Saturday"
    elif numb == 7:
        return "Sunday"
    else:
        return "Error"


number = int(input())
result = day_of_week(number)
print()
