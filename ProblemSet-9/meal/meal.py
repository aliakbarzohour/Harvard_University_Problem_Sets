
# The convert function converts the input time to a decimal format
def convert(time):
    hour, minute = time.split(":")
    return float(hour) + float(minute)/60

def main():
    # Request time input from user
    time = input("Please enter a time in 24-hour format (e.g. 7:30 or 15:45): ")
    # Initialize meal_time variable
    meal_time = ""
    # Convert input time to decimal format
    t = convert(time)

    # Check for breakfast time
    if t >= 7 and t < 8:
        meal_time = "breakfast time"
    # Check for lunch time
    elif t >= 12 and t <= 13:
        meal_time = "lunch time"
    # Check for dinner time
    elif t >= 18 and t < 19:
        meal_time = "dinner time"

    # Print the meal time if it exists
    if meal_time != "":
        print(meal_time)

if __name__ == "__main__":
    main()