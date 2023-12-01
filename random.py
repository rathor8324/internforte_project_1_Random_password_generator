python
import string
import random

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_punctuation):
    characters = ""
    
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation

    if not characters:
        print("Error: Select at least one character type.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_user_preferences():
    try:
        length = int(input("Enter the desired password length: "))
        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include numbers? (y/n): ").lower() == 'y'
        use_punctuation = input("Include punctuation? (y/n): ").lower() == 'y'

        return length, use_uppercase, use_lowercase, use_digits, use_punctuation

    except ValueError:
        print("Error: Please enter a valid number for the password length.")
        return None

if __name__ == "__main__":
    preferences = get_user_preferences()

    while preferences is None:
        preferences = get_user_preferences()

    password = generate_password(*preferences)

    if password:
        print("Generated Password:", password)
