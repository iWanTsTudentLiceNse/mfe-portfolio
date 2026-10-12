# Day4 Buying Decision Considering Total Cost
# current_balance = float(input("Current Balance:"))
current_balance = 55000
purchase_amounts = [12000, 8000, 15000]
total_cost = 0

purchase_amounts[1] = 9000
purchase_amounts.append(5000)

for price in purchase_amounts:
    total_cost = total_cost + price

can_buy = current_balance - total_cost >= 20000

print(total_cost, can_buy)
