# Day 2 - Conditional Statements and Return Classification
initial_price = float(input("Initial price: "))
final_price = float(input("Final price: "))

return_percentage = ((final_price-initial_price)/initial_price)*100
printing_percentage = round(return_percentage,3)

if return_percentage >= 10:
    status = "Excellent"
elif return_percentage >= 5:
    status = "High Profit"
elif return_percentage > 0:
    status = "Profit"
elif return_percentage == 0:
    status = "Break Even"
elif return_percentage > -5:
    status = "Loss"
else:
    status = "High Loss"
print("Status:", status)
print("Return:", printing_percentage, "%")