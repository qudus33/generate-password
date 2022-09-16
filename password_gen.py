# import sample function from random module
from random import sample

# Get password values
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
special_char = "!@#$%^&*"
password_length = int(input("Enter the password length [e.g 8]: "))

# Generate password
password = upper_case + lower_case + numbers + special_char
password = "".join(sample(password, password_length))
print(f"Your password is: {password}")