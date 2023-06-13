num1, operator, num2 = input("Enter an expression in the format 'num1 operator num2': ").split()
num1 = int(num1)
num2 = int(num2)
result = 0

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2

print(round(result, 1))
