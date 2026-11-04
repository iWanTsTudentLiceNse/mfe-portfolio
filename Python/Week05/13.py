products = [
    {"name": " Pen ", "qty": 2},
    {"name": "pen", "qty": 3},
    {"name": " BOOK ", "qty": 1}
]

cleaned = []
for product in products:
    copied = product.copy()
    copied["name"] = copied["name"].strip().lower()
    cleaned.append(copied)

totals = {}
for product in cleaned:
    name = product["name"]
    if name in totals:
        totals[name] += product["qty"]
    else:
        totals[name] = product["qty"]

print(products[0]["name"])
print(totals)

cleaned[0]["qty"] = 10

print(products[0]["qty"])
print(cleaned[0]["qty"])