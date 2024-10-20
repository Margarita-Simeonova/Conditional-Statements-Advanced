def trade_commissions(city: str, sales: float):

    if city == "Sofia":

        if 0 <= sales <= 500:
            commission = sales * 0.05
        elif 500 < sales <= 1000:
            commission = sales * 0.07
        elif 1000 < sales <= 10000:
            commission = sales * 0.08
        elif sales > 10000:
            commission = sales * 0.12
        else:
            return "error"

    elif city == "Varna":

        if 0 <= sales <= 500:
            commission = sales * 0.045
        elif 500 < sales <= 1000:
            commission = sales * 0.075
        elif 1000 < sales <= 10000:
            commission = sales * 0.1
        elif sales > 10000:
            commission = sales * 0.13
        else:
            return "error"

    elif city == "Plovdiv":

        if 0 <= sales <= 500:
            commission = sales * 0.055
        elif 500 < sales <= 1000:
            commission = sales * 0.08
        elif 1000 < sales <= 10000:
            commission = sales * 0.12
        elif sales > 10000:
            commission = sales * 0.145
        else:
            return "error"

    else:
        return f"error"

    return f"{commission:.2f}"


city = input()
sales = float(input())
result = trade_commissions(city, sales)
print(result)
