"""
Beginner Python Practice: Simple Calculator

Concepts covered:
- Variables
- Functions
- if / elif / else
- while loop
- Basic input/output
- try/except for handling bad input
"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: cannot divide by zero"
    return a / b


def main():
    print("=== Simple Calculator ===")
    print("Operations: + - * /")
    print("Type 'quit' to exit\n")

    while True:
        first = input("Enter first number (or 'quit'): ")
        if first.lower() == "quit":
            print("Goodbye!")
            break

        operator = input("Enter operator (+, -, *, /): ")
        second = input("Enter second number: ")

        try:
            num1 = float(first)
            num2 = float(second)
        except ValueError:
            print("That's not a valid number. Try again.\n")
            continue

        if operator == "+":
            result = add(num1, num2)
        elif operator == "-":
            result = subtract(num1, num2)
        elif operator == "*":
            result = multiply(num1, num2)
        elif operator == "/":
            result = divide(num1, num2)
        else:
            print("Unknown operator. Please use + - * /\n")
            continue

        print(f"Result: {result}\n")


if __name__ == "__main__":
    main()
