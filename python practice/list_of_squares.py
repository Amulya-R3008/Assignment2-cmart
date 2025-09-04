# Program to create a list of squares from user input with validation

# Take input from user (numbers separated by space)
user_input = input("Enter numbers separated by space: ")

numbers = []
for x in user_input.split():        # breaks the string into separate parts wherever there’s a space (by default)
    if x.isdigit():                 # check if input is a digit
        numbers.append(int(x))      # convert to integer
    else:
        print(f"Invalid input ignored: {x}")

# Create a list of squares
squares = []
for x in numbers:
    squares.append(x**2)

if numbers:   # check if list is not empty
    print("Original List:", numbers)
    print("Squares:", squares)
else:
    print("No valid numbers entered")
