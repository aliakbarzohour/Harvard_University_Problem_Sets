# =======================================================

# What should I have done?

# Write a program that prompts the user for a greeting.
# If the user is greeted withIf "hello" starts,
# the output of the program will be $0, and if it starts
# with the first letter "h" (but not "hello"),
# the program will output $20. Otherwise,
# the output will be $100.

# =======================================================

# Get user input as response
response = input("[?] Hello ? : ")
# Check if response is "hello" or "Hello"
if response == "hello" or response == "Hello":
    # Print "$0" if response is "hello" or "Hello"
    print("$0")
elif response[0] == "h":
    # If response starts with "h", print "$20"
    print("$20")
else:
    # If neither condition above is met, print "$100"
    print("$100")
