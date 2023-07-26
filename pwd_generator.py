import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    # Combine character sets based on criteria
    valid_chars = letters
    if numbers:
        valid_chars += digits
    if special_characters:
        valid_chars += special

    pwd = ""
    meets_criteria = False
    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(valid_chars)
        pwd += new_char

        # Check if the password meets all the criteria
        has_numbers = any(char.isdigit() for char in pwd)
        has_special_characters = any(char in special for char in pwd)
        meets_criteria = has_numbers if numbers else True
        meets_criteria &= has_special_characters if special_characters else True

    return pwd

# Generate a password of at least 10 characters with numbers and special characters
password = generate_password(10, numbers=True, special_characters=True)
print(password)
