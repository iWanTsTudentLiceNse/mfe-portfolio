def parse_item(line, sep=","):
    """Parse item name and quantity from line and return tuple"""
    name, quantity = line.split(sep)
    name = name.strip().lower()
    return name, int(quantity)

def total_quantity(*lines):
    total = 0
    for line in lines:
        name, quantity = parse_item(line)
        total = total + quantity
    return total

def show_counts(**counts):
    print(counts)

get_quantity = lambda item: item[1]

line = input("Item Name,Quantity: ")
print(parse_item(line))

f = open("C:/Users/user/Documents/MFE_Preparation_Git/Python/Week06/day15_input.txt", "w", encoding="utf-8")
f.write('MILK, 0' + "\n")
f = open("C:/Users/user/Documents/MFE_Preparation_Git/Python/Week06/day15_input.txt", "r", encoding="utf-8")
saved_line = f.readline()
f.close()
print(parse_item(saved_line))
f.close()

print(parse_item("MILK;3",sep=";"))
print(parse_item("BOOK, 0\n"))
print(total_quantity(" Pen , 2", "BOOK, 3"))
show_counts(pen=2,book=3)

with open("C:/Users/user/Documents/MFE_Preparation_Git/Python/Week06/day15_input.txt", "a", encoding="utf-8") as f:
    f.write("BOOK, 3\n")

total = 0
with open("C:/Users/user/Documents/MFE_Preparation_Git/Python/Week06/day15_input.txt", "r", encoding="utf-8") as f:
    for line in f:
        name, quantity = parse_item(line)
        total += quantity

with open("C:/Users/user/Documents/MFE_Preparation_Git/Python/Week06/day15_total.txt", "w", encoding="utf-8") as f:
    f.write(str(total))

print(total)