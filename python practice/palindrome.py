# Function to check palindrome
def is_palindrome(s):
    s = s.lower()            # ignore case
    return s == s[::-1]      # check if same as reverse

user_input = input("Enter a string: ").strip() # take user input
#strip() used to remove extra spaces

if not user_input:           # check for empty input
    print("Input cannot be empty")
elif is_palindrome(user_input):
    print("Palindrome")
else:
    print("Not a palindrome")
