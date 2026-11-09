import sys
print(sys.argv)

def parse_item(line, sep=","):
    """Parse item name and quantity from line and return tuple"""
    name, quantity = line.split(sep)
    name = name.strip().lower()
    return name, int(quantity)

total = 0
with open(sys.argv[1], "r", encoding="utf-8") as f:
    for line in f:
        name, quantity = parse_item(line)
        total = quantity + total

with open(sys.argv[2], "w", encoding="utf-8") as g:
    g.write(str(total))