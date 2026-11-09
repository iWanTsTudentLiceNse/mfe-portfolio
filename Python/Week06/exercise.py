def parse_line(line, sep=","):
    name, quantity = line.split(sep)
    name = name.lower().strip()
    return name, int(quantity.strip())


with open("C:/Users/user/Documents/MFE_Preparation_Git/Python/Week06/day15_expenses_clean.txt", "w", encoding="utf-8") as h:
    with open("C:/Users/user/Documents/MFE_Preparation_Git/Python/Week06/day15_expenses_raw.txt", "r", encoding="utf-8") as g:
        for line in g:
            if line.strip() == "":
                continue
            else:
                name, quantity = parse_line(line)
                h.write(f"{name},{quantity}\n")

total = 0
with open("C:/Users/user/Documents/MFE_Preparation_Git/Python/Week06/day15_expenses_clean.txt", "r", encoding="utf-8") as f:
    for line in f:
        name, quantity = parse_line(line)
        total = total + quantity


with open("C:/Users/user/Documents/MFE_Preparation_Git/Python/Week06/day15_expenses_total.txt", "w", encoding="utf-8") as i:
    i.write(str(total))

