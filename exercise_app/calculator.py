# Simple Calculator Program using Functions

# Define the functions for each operation
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b

def power(a, b):
    return a ** b

def modulus(a, b):
    return a % b


# Display menu for the user
def display_menu():
    print("\n===== SIMPLE CALCULATOR =====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (^)")
    print("6. Modulus (%)")
    print("7. Exit")
    print("=============================")


# Main program
def main():
    while True:
        display_menu()
        
        choice = input("Choose an operation (1-7): ")

        if choice == '7':
            print("Exiting calculator... Goodbye! 👋")
            break

        # Validate user input
        if choice not in ['1', '2', '3', '4', '5', '6']:
            print("Invalid choice! Please enter a number between 1 and 7.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values only.")
            continue

        # Perform selected operation
        if choice == '1':
            result = add(num1, num2)
            symbol = '+'
        elif choice == '2':
            result = subtract(num1, num2)
            symbol = '-'
        elif choice == '3':
            result = multiply(num1, num2)
            symbol = '*'
        elif choice == '4':
            result = divide(num1, num2)
            symbol = '/'
        elif choice == '5':
            result = power(num1, num2)
            symbol = '^'
        elif choice == '6':
            result = modulus(num1, num2)
            symbol = '%'

        print(f"\nResult: {num1} {symbol} {num2} = {result}\n")


# Run the calculator
if __name__ == "__main__":
    main()
