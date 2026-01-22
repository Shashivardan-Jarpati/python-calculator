# Simple Python Calculator

print("🔢 SIMPLE CALCULATOR")
print("-------------------")

# Take inputs from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nChoose operation:")
print("+  Addition")
print("-  Subtraction")
print("*  Multiplication")
print("/  Division")
print("%  Modulus")

operation = input("Enter operation (+, -, *, /, %): ")

# Perform calculation
if operation == "+":
    result = num1 + num2

elif operation == "-":
    result = num1 - num2

elif operation == "*":
    result = num1 * num2

elif operation == "/":
    if num2 == 0:
        print("❌ Error: Division by zero is not allowed")
        exit()
    result = num1 / num2

elif operation == "%":
    result = num1 % num2

else:
    print("❌ Invalid operation selected")
    exit()

# Display result
print("\n✅ Result:")
print(f"{num1} {operation} {num2} = {result}")
