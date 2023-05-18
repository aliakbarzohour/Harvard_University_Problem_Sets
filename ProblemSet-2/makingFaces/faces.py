# ===============================================

# What should I have done?

# Write a function called convert that takes a string (str) as input
# receives and converts every :) to 🙂 and every :( to 🙁 and returns
# the same input and the rest of the text remains unchanged.
# Then, in the same file, implement a function named main that asks the
# user for input, then calls the convert function and displays the output
# by transferring the user's input to that function.
# [!] Don't forget to call the main function at the bottom of your file.

# ===============================================

def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text


def main():
    text = input("[*] Type Your Feeling : ")
    converted_text = convert(text)
    print(converted_text)


main()

# OutPut :

# [*] Type Your Feeling : Im Happy :)
# Im Happy 🙂
