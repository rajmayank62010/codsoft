import random
import string

def generate_password(length, complexity):
    """Generates a random password of the specified length and complexity.

    Args:
        length: The desired length of the password.
        complexity: An integer indicating the level of complexity (1-3).

    Returns:
        A randomly generated password string.
    """

    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    if complexity == 1:
        char_set = letters
    elif complexity == 2:
        char_set = letters + digits
    else:
        char_set = letters + digits + symbols

    password = ''.join(random.choice(char_set) for _ in range(length))
    return password

if __name__ == "__main__":
    password_length = int(input("Enter the desired password length: "))
    complexity_level = int(input("Enter the complexity level (1-4): "))

    if complexity_level not in range(1, 5):
        print("Invalid complexity level. Please enter a value between 1 and 4.")
    else:
        password = generate_password(password_length, complexity_level)
        print("Generated Password:", password)