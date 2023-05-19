# =================================================================================
# === "Forty-two," Deep Thought said in an infinitely calm and majestic tone. » ===
# =================================================================================

# What should I have done?

# Write a program that answers the user's 
# "ultimate question about life, the world, and everything."
# If the user's input is "42" or "forty-two" or "forty-two" 
# (regardless of capital or small letters), the output of 
# the program will be yes. Otherwise, the output 
# of the program will be No.

# =================================================================================

def deep():
    user_input = input("[?] The ultimate question about life, the world and everything :").lower().replace(" ", "")
    # Check if the user's input is equal to any of the pre-defined values for the answer to the ultimate question. If it is,
    # print "Yes", otherwise print "No".
    if user_input == "42" or user_input == "fortytwo" or user_input == "forty-two" or user_input == "Forty Two" or user_input == "Forty-two":
        print("Yes")
    else:
        print("No")

deep()
