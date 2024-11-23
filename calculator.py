def add(a, b):
    """Adds two numbers."""
    return a + b

def subtract(a, b):
    """Subtracts the second number from the first."""
    return a - b

def multiply(a, b):
    """Multiplies two numbers."""
    return a * b

def divide(a, b):
    """Divides the first number by the second. Handles division by zero."""
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def temp_converter(celsius):
    """Converts Celsius to Fahrenheit."""
    return celsius * (9 / 5) + 32

def calculator(num1, num2, operator):
    """Performs basic mathematical operations based on the given operator."""
    if operator == '+':
        return add(num1, num2)
    elif operator == '-':
        return subtract(num1, num2)
    elif operator == '*':
        return multiply(num1, num2)
    elif operator == '/':
        return divide(num1, num2)
    else:
        return "Error: Invalid operator."

def main():
    """Main program function to interact with the user."""
    print("Welcome to the Calculator!")
    print("Choose an operation: basic math (+, -, *, /) or temperature conversion (T).")
    try:
        option = input("Enter 'M' for math or 'T' for temperature conversion: ").strip().upper()

        if option == 'M':
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
            operator = input("Enter your operator (+, -, *, /): ").strip()
            result = calculator(num1, num2, operator)
            print(f"Result: {result}")

        elif option == 'T':
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = temp_converter(celsius)
            print(f"{celsius}°C is equivalent to {fahrenheit}°F.")

        else:
            print("Error: Invalid choice. Please restart and select a valid option.")

    except ValueError:
        print("Error: Invalid input. Please enter numeric values where required.")

# Run the program
main()