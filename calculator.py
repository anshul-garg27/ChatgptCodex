#!/usr/bin/env python3

"""Simple command-line calculator."""

def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference of a and b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return the quotient of a and b. Raises ValueError on division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def main():
    """Run a simple REPL for the calculator."""
    while True:
        op = input("Enter operation (+, -, *, /) or 'q' to quit: ").strip()
        if op.lower() == 'q':
            break
        if op not in ('+', '-', '*', '/'):
            print('Invalid operation')
            continue
        try:
            a = float(input('Enter first number: '))
            b = float(input('Enter second number: '))
        except ValueError:
            print('Invalid number')
            continue
        try:
            if op == '+':
                result = add(a, b)
            elif op == '-':
                result = subtract(a, b)
            elif op == '*':
                result = multiply(a, b)
            else:
                result = divide(a, b)
            print('Result:', result)
        except Exception as exc:
            print('Error:', exc)


if __name__ == '__main__':
    main()
