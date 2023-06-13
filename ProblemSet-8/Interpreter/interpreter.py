# ==============================================================

# What should I have done?

# ?

# ==============================================================

# Request an expression in the format 'num1 operator num2' from user
num1, operator, num2 = input("Enter an expression in the format 'num1 operator num2': ").split()
# Convert the inputs to integers
num1 = int(num1)
num2 = int(num2)
# Initialize result variable
result = 0

# Check for addition operation
if operator == "+":
    result = num1 + num2
# Check for subtraction operation
elif operator == "-":
    result = num1 - num2
# Check for multiplication operation
elif operator == "*":
    result = num1 * num2
# Check for division operation
elif operator == "/":
    result = num1 / num2

# Print the result rounded to one decimal place
print(round(result, 1))
