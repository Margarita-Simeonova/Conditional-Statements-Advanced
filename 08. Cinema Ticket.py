def cinema_ticket(day):

    if day == "Monday" or day == "Tuesday" or day == "Friday":
        return 12
    elif day == "Wednesday" or day == "Thursday":
        return 14
    else:
        return 16


day_of_week = input()
print(cinema_ticket(day_of_week))
