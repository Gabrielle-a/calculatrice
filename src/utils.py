def add(*args):
    """Return the sum of all numbers in args."""
    print("TRACE:add args=", args) 
    total = 0
    for x in args:
        total += x
    return total


def subtract(*args):
    """
    Subtract all subsequent numbers from the first.
    subtract(10, 1, 2) -> 7
    """
    if not args:
        raise ValueError("subtract() requires at least one number")
    result = args[0]
    for x in args[1:]:
        result -= x
    return result

def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
