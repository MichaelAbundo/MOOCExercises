number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))
operation = str(input("Operation:"))

if operation == "add":
    print(number1, "+", number2, "=", (number1 + number2))
elif operation == "multiply":
    print(number1, "*", number2, "=", (number1 * number2))
elif operation == "subtract":
    print(number1, "-", number2, "=", (number1 - number2))