#Calculate return in percentage

buy_price = float(input("Enter the purchase price: "))
sell_price = float(input("Enter the selling price: "))

yield = (sell_price - buy_price) / buy_price * 100
yield = round(yield, 2)

print("Yield: ", yield, "%")