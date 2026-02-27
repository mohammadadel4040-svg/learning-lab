# Week 5 - Modular Password Validator
# This program checks password strength using functions and modules

import string
import random


# Password Rule Functions

# Check minimum password length
def check_min_length(password, min_len=8):
    return len(password) >= min_len


# Check uppercase letters
def has_uppercase(password):
    return any(char in string.ascii_uppercase for char in password)


# Check lowercase letters
def has_lowercase(password):
    return any(char in string.ascii_lowercase for char in password)


# Check digits
def has_digit(password):
    return any(char in string.digits for char in password)


# Check special characters
def has_special_char(password):
    return any(char in string.punctuation for char in password)


# Master Validation Function

def validate_password(password):

    results = {
        "min_length": check_min_length(password),
        "uppercase": has_uppercase(password),
        "lowercase": has_lowercase(password),
        "digit": has_digit(password),
        "special_char": has_special_char(password)
    }

    # Password is valid only if ALL checks pass
    results["is_valid"] = all(results.values())

    return results


# Main Program 

def main():

    print("=" * 40)
    print("PASSWORD STRENGTH CHECKER")
    print("=" * 40)

    password = input("Enter a password: ")

    results = validate_password(password)

    print("\nValidation Results:")

    for rule, status in results.items():
        print(f"{rule}: {status}")

    if results["is_valid"]:
        print("\n✅ Strong Password!")
    else:
        hints = [
            "Try adding numbers.",
            "Use uppercase letters.",
            "Add special symbols like !@#",
            "Increase password length."
        ]
        print("\n❌ Weak password.")
        print("Hint:", random.choice(hints))


# Run program
if __name__ == "__main__":
    main()
