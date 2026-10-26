def calculate_return(sell_price, buy_price = 10000):
    if buy_price <= 0 or sell_price < 0:
        raise ValueError("Input valid number")
    margin = sell_price - buy_price
    yield_percent = (margin/buy_price)*100
    return margin, yield_percent

prices = [11000, 10000, 0, -100, 9000]

for price in prices:
    try :
        a = calculate_return(price, )
        print(a)
    except ValueError as error :
        print(error)


def read_amount(message):
    while True:
        x = input(message)

        try:
            price = int(x)
        except ValueError:
            print("Enter Valid Number")
            continue

        if price < 0:
            print("Enter Valid Number")
            continue

        return price

def check_budget(budget, spent):
    if budget < 0 or spent < 0 :
        raise ValueError("Seriously??")
    left = budget - spent
    if left > 0:
        return left, "Within budget"
    elif left == 0:
        return left, "Exactly on budget"
    else:
        return left, "Over budget"

budget = read_amount("Budget: ")
spent = read_amount("Spent: ")
result = check_budget(budget, spent)
print(result)


