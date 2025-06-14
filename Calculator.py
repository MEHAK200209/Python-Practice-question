def calculator(a, b, operation):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        return a / b if b != 0 else "Cannot divide by zero"
    else:
        return "Invalid operation"

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    operation = input("Enter operation (add, subtract, multiply, divide): ").lower()

    result = calculator(a, b, operation)
    print("Result:", result)
except ValueError:
    print("Invalid input! Please enter numeric values.")