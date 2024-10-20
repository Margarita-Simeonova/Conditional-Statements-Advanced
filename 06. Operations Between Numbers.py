def operations_between_numbers(number1, number2, operator):

    result = 0

    if operator == "+":
       result = number1 + number2
    elif operator == "-":
        result = number1 - number2
    elif operator == "*":
        result = number1 * number2
    elif operator == "/" and not number2 == 0:
        return f"{number1} {operator} {number2} = {number1 / number2:.2f}"
    elif (operator == "/" or operator == "%") and number2 == 0:
        return f"Cannot divide {number1} by zero"
    elif operator == "%":
        return f"{number1} {operator} {number2} = {number1 % number2}"

    if result:
        if result % 2 == 0:
            even_or_odd = "even"
        else:
            even_or_odd = "odd"
        return f"{number1} {operator} {number2} = {result} - {even_or_odd}"


num_1 = int(input())
num_2 = int(input())
operator = input()
result = operations_between_numbers(num_1, num_2, operator)
print(result)
