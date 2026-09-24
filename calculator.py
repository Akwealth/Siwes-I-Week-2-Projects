# Simple Calculator Program

print("Calculator App")
print("Enter your choice of operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

# Step 1: Get choice from user
choice = input("Enter choice (1, 2, 3, or 4): ")

# Step 2: Validate choice and perform calculations
if choice in ('1', '2', '3', '4'):
    # Get numbers from the user and convert to float for decimal support
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}")

    elif choice == '2':
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}")

    elif choice == '3':
        result = num1 * num2
        print(f"Result: {num1} * {num2} = {result}")

    elif choice == '4':
        # Edge-case handling: prevent division by zero
        if num2 == 0:
            print("Error! Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"Result: {num1} / {num2} = {result}")

else:
    print("Invalid Input! Please select a valid option (1-4).")
