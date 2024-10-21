def on_time_for_exam(exam_h, exam_m, hour, minutes):

    exam_time_in_minutes = exam_h * 60 + exam_m
    time_in_minutes = hour * 60 + minutes
    total_time = exam_time_in_minutes - time_in_minutes

    if total_time == 0:
        return "On time"
    elif exam_time_in_minutes - 30 <= time_in_minutes <= exam_time_in_minutes:
        return f"On time {total_time} minutes before the start"
    elif exam_time_in_minutes > time_in_minutes:
        print("Early")
        total_minutes = exam_time_in_minutes - time_in_minutes
        if total_minutes < 60:
            return f"{total_minutes} minutes before the start"
        else:
            hours = total_minutes // 60
            minutes = total_minutes % 60
            if minutes < 10:
                return f"{hours}:0{minutes} hours before the start"
            else:
                return f"{hours}:{minutes} hours before the start"
    else:
        print("Late")
        total_minutes = time_in_minutes - exam_time_in_minutes
        hours = total_minutes // 60
        minutes = total_minutes % 60
        if total_minutes < 60:
            return f"{total_minutes} minutes after the start"
        if minutes < 10:
            return f"{hours}:0{minutes} hours after the start"
        else:
            return f"{hours}:{minutes} hours after the start"


exam_h = int(input())
exam_m = int(input())
hour = int(input())
minute = int(input())
print(on_time_for_exam(exam_h, exam_m, hour, minute))
