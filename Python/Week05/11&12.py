rows = [" Pen|2 ", "pen|3", " BOOK | 1 "]
totals = {}

for row in rows:
    name_text, qty_text = row.split("|")
    name = name_text.strip().lower()
    qty = int(qty_text.strip())
    if name in totals:
        qty = qty + totals[name]
    totals[name] = qty

print(totals)


parts = []
for name, qty in totals.items():
    parts.append(f"{name}={qty}")

print(", ".join(parts))