stock = {
    "apple": 10,
    "banana": 5
}
for fruit, n in stock.items():
    print(fruit, n)

stock["apple"] = 7
stock["orange"] = 8
del stock["banana"]

print("grape" in stock)
print(stock.get("grape", "Not found"))

for fruit, n in stock.items():
    print(fruit, n)

products = [
    {"name": "pen", "price": 1200, "quantity": 3},
    {"name": "notebook", "price": 3000, "quantity": 2},
    {"name": "eraser", "price": 500, "quantity": 0}
]

empty = []
#total = 0
#for product in products:
#    if product["quantity"] > 0:
#        print(product["name"], product["price"]*product["quantity"])
#        total = total + product["price"]*product["quantity"]
#print("total", total)

def calculate_total(products):
    total = 0
    count = 0
    for product in products:
        if product["quantity"] > 0:
            total = total + product["price"]*product["quantity"]
            count = count + 1
    return total, count

products[0]["quantity"] = 5
total, count = calculate_total(products)
print(total, count)
total, count = calculate_total(empty)
print(total, count)

names = ["pen", "notebook", "pen", "eraser"]
seen = set()

for name in names:
    if name in seen:
        print("Duplicate:", name)
    else:
        seen.add(name)

print(len(seen))
