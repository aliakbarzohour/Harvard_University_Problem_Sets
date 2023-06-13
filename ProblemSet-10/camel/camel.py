variable_name = input("Enter your variable name in CamelCase: ")

# Convert the first character of the variable name to lowercase
snake_case_variable_name = variable_name[0].lower()

# Loop through the rest of the characters in the variable name
for i in range(1, len(variable_name)):
    # If the character is uppercase, add an underscore before converting it to lowercase
    if variable_name[i].isupper():
        snake_case_variable_name += '_'
        snake_case_variable_name += variable_name[i].lower()
    else:
        snake_case_variable_name += variable_name[i]

print(snake_case_variable_name)
