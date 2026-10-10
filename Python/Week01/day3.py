#Day3 Buying Decision
current_balance = float(input("Current Balance:"))
price = float(input("Price: "))
Qty = int(input("Qty: "))

total_cost = price*Qty
can_buy = current_balance > total_cost and (current_balance - total_cost) >= 20000

if can_buy :
    print("Buy")
else :
    print("Wait")