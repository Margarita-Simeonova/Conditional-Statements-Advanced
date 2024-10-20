PREMIERE = 12
NORMAL = 7.5
DISCOUNT = 5


def cinema(ticket_type, rows, columns):

    price = 0
    if ticket_type == "Premiere":
        price = rows * columns * PREMIERE
    elif ticket_type == "Normal":
        price = rows * columns * NORMAL
    else:
        price = rows * columns * DISCOUNT

    return f"{price:.2f}"


ticket_type = input()
rows = int(input())
columns = int(input())
print(cinema(ticket_type, rows, columns))
