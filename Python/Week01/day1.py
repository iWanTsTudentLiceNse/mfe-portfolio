#Calculate return in percentage

buy_price = float(input("Enter the purchase price: "))
sell_price = float(input("Enter the selling price: "))

return_percentage = (sell_price - buy_price) / buy_price * 100
return_percentage = round(return_percentage, 2)

print("Yield: ", return_percentage, "%")