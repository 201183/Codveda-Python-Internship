def add(a, b):# Function definitions
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed"
    return a / b
# Taking input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Choose operation:")
print("+ for Addition")
print("- for Subtraction")
print("* for Multiplication")
print("/ for Division")
# Performing calculation
choice = input("Enter your choice: ")
if choice == "+":
    print("Result:", add(num1, num2))
elif choice == "-":
    print("Result:", subtract(num1, num2))
elif choice == "*":
    print("Result:", multiply(num1, num2))
elif choice == "/":
    print("Result:", divide(num1, num2))
else:
    print("Invalid operation selected")
