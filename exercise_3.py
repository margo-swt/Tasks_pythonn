import random
import string


def generate_password():
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    numbers = string.digits
    special_chars = string.punctuation

    all_chars = lowercase_letters + uppercase_letters + numbers + special_chars

    password = ''
    length = int(input("Enter the size of password (max 8 character): "))

    for i in range(length):
        if length > 8:
            print("password must be max 8 character")
            break
        password += random.choice(all_chars)

    return password


password = generate_password()
print(password)
