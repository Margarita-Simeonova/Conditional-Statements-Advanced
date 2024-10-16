def weekend_or_work_day(week_day):

    if week_day == "Monday" or week_day == "Tuesday" or week_day == "Wednesday" or week_day == "Thursday" or week_day == "Friday":
        return "Working day"
    elif week_day == "Saturday" or week_day == "Sunday":
        return "Weekend"

    else:
        return "Error"


day = input()
print(weekend_or_work_day(day))
