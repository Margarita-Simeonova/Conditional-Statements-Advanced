def invalid_number(numb):

    if not 100 <= numb <= 200 and not numb == 0:
        print("invalid")


number = int(input())
invalid_number(number)
