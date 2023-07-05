def remove_vowels(text):
    # Define a string of vowels to remove from the text
    vowels = "AEIOUaeiou"
    # Use a list comprehension to filter out the vowels and join the remaining characters into a new string
    return "".join([char for char in text if char not in vowels])

# Get user input for the text to be processed
text = input("Enter your text: ")
# Split the input text into a list of words
words = text.split()

# Loop through each word in the list of words
for word in words:
    # Print the result of removing vowels from the current word, with a space as the separator
    print(remove_vowels(word), end=" ")

# Output a newline character at the end of the program
print()
