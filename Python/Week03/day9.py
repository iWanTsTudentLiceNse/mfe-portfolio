# Coach-provided review example, read and understood by the learner.

def calculate_return(buy_price, sell_price):
    if buy_price <= 0:
        raise ValueError("Buy price must be positive.")
    if sell_price < 0:
        raise ValueError("Sell price cannot be negative.")

    profit = sell_price - buy_price
    return_rate = profit / buy_price * 100
    return profit, return_rate


prices = [11000, 10000, 9000, -100]

for sell_price in prices:
    try:
        profit, rate = calculate_return(10000, sell_price)
        print("Profit:", profit, "Return (%):", rate)
    except ValueError as error:
        print(error)
