"""
Simple Calculator App
----------------------
A basic command-line calculator that supports addition, subtraction,
multiplication, division, and more.
"""

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def power(x, y):
    return x ** y

def modulus(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x % y


def get_number(prompt):
    """Keep asking until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")


def main():
    operations = {
        "1": ("Addition (+)", add),
        "2": ("Subtraction (-)", subtract),
        "3": ("Multiplication (*)", multiply),
        "4": ("Division (/)", divide),
        "5": ("Power (^)", power),
        "6": ("Modulus (%)", modulus),
    }

    print("=" * 35)
    print("        SIMPLE CALCULATOR")
    print("=" * 35)

    while True:
        print("\nSelect an operation:")
        for key, (label, _) in operations.items():
            print(f"  {key}. {label}")
        print("  0. Exit")

        choice = input("\nEnter choice: ").strip()

        if choice == "0":
            print("Goodbye!")
            break

        if choice not in operations:
            print("Invalid choice. Please try again.")
            continue

        label, func = operations[choice]
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        result = func(num1, num2)
        print(f"\nResult: {num1} {label.split('(')[1].strip(')')} {num2} = {result}")


if __name__ == "__main__":
    main()
