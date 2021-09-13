def add(a, b):
    """This function takes to values and returns their sum."""

    print(f"Adding {a} + {b}")
    return a + b


def subtract(a, b):
    """This function takes to values and returns their subtraction."""

    print(f"Subtraction {a} - {b}")
    return a - b


def multiply(a, b):
    """This function takes to values and returns their product."""

    print(f"Multiplying {a} * {b}")
    return a * b


def divide(a, b):
    """This function takes to values and returns their quotient."""

    print(f"Dividing {a} / {b}")
    return a / b


age = add(20, 10)
height = subtract(200, 50)
weight = multiply(55, 3)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, Iq: {iq}")
print("Puzzle")
result = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print(f"Result: {result}")