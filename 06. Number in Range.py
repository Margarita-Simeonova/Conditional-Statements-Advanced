def number_in_range(numb):

    if -100 <= numb <= 100 and not numb == 0:
        return "Yes"
    else:
        return "No"


number = int(input())
print(number_in_range(number))
