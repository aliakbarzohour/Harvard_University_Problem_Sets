# ===============================================

# What should I have done?

# 1 - dollars_to_float which should accept a string as input
# (format ##.##$ where each # is a digit of a decimal number),
# remove the $ sign in front of it and return the amount as a float.
# As For example, when we enter $50.00 as input, the function
# should return the value 50.0.

# 2 - percent_to_float which should accept a string as input
# (format %## where each # is a digit of a decimal number),
# remove the % sign in front of it and return the percentage as a float.
# For example, We give %15 as input and the function should give
# us 0.15 as output.

# ❖ Assume that the user enters the input values in
#   the above mentioned formats.

# ===============================================

def main():
    # Prompting the user for the cost of the meal and tip percentage
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))

    # Calculating the tip
    tip = dollars * percent

    # Printing the result with two decimal places
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # Removing dollar sign and converting to float
    return float(d.replace('$', '').strip())


def percent_to_float(p):
    # Removing percent sign, converting to float, and dividing by 100
    return float(p.replace('%', '').strip()) / 100


# Calling the main function to run the program
main()
