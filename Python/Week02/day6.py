# Compare independent budgets, buy at most two items, and verify spending.
products = ["A", "B", "C", "D"]
prices = [12000, 8000, 15000, 5000]
budgets = [50000, 18000, 0]
purchase_results = []
remaining_balances = []
selected_budget = []

for i in range(len(budgets)):
    balance = budgets[i]
    bought = []
    spent = 0
    for j in range(len(prices)):
        if balance >= prices[j]:
            balance = balance - prices[j]
            spent = spent + prices[j]
            bought.append(products[j])
        if len(bought) == 2:
            break
    remaining_balances.append(balance)
    purchase_results.append(bought)
    print(budgets[i], spent, budgets[i] - balance, spent == budgets[i] - balance)
    print(budgets[i], purchase_results[i], remaining_balances[i])

print(purchase_results)
print(remaining_balances)

for k in range(len(budgets)):
    print(budgets[k], len(purchase_results[k]))

for l in range(len(budgets)):
    if len(purchase_results[l]) == 2 and remaining_balances[l] >= 5000:
        selected_budget.append(budgets[l])
print(selected_budget)
