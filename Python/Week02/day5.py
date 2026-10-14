# Buy items in order when the balance is sufficient, and track purchases.
balance = 20000
purchases = [12000, 9000, 8000]
count = 0
bought = []

for price in purchases:
    if balance >= price:
        balance = balance - price
        count = count + 1
        bought.append(price)
    else:
        print("Can't Buy")

print(balance, count, bought)


# Summarize daily and overall payments, skipping negatives and stopping each day at the first zero.
daily_payments = [
    [12000, -3000, 8000],
    [5000, 0, 15000],
    [],
    [9000, -1000, 3000]
]
total = 0
count = 0

for payments in daily_payments:
    daily_count = 0
    daily_total = 0
    for payment in payments:
        if payment > 0:
            total = total + payment
            daily_total = daily_total + payment
            count = count + 1
            daily_count = daily_count + 1
        elif payment == 0:
            break
    print(daily_total, daily_count)
print(total, count)
