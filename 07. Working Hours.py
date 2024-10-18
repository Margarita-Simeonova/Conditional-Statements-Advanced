def work_time(hour, day):

    if day == "Sunday":
        return "closed"

    elif 10 <= hour < 18:
        return "open"

    else:
        return "closed"


day_hour = int(input())
day_of_week = input()
print(work_time(day_hour, day_of_week))
