# 1. Quantity input and total cost

def total_cost(unit_price, qtty):
    return unit_price * qtty


def read_QUANTITY():
    while True:
        x = input("Qtty: ")

        try:
            qtty = int(x)
        except ValueError:
            print("Enter an integer.")
            continue

        if qtty <= 0:
            print("Enter a positive integer.")
            continue

        return qtty


x = total_cost(2500, read_QUANTITY())
print("Total:", x)


# 2. Input validation with raise

def total_cost(unit_price, quantity):
    if quantity <= 0:
        raise ValueError("Quantity must be positive.")
    elif unit_price < 0:
        raise ValueError("Unit price cannot be negative.")

    return unit_price * quantity


try:
    quantity = int(input("Qtty: "))
    unit_price = int(input("Price: "))
    x = total_cost(unit_price, quantity)
    print(x)
except ValueError as error:
    print(error)
