def check_budget(budget, spent):
    if budget < 0 or spent < 0:
        raise ValueError("Amounts cannot be negative")
    else:
        balance = budget - spent

    if balance > 0 :
        return balance, "Within Budget"
    elif balance == 0:
        return balance, "Exactly on budget"
    else:
        return balance, "Over budget"


try:
    budget = int(input("Please input expected budget: "))
    spent = int(input("Please input expected payment: "))
    x = check_budget(budget, spent)
    print(x)
except ValueError as error:
    print(error)
