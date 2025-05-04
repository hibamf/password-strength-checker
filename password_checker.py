import string

def check_password_strength(password):
    score = 0
    length = len(password)

    if length >= 8:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score == 3 or score == 4:
        return "Moderate"
    else:
        return "Strong"

# Main function
def main():
    print("🔐 Password Strength Checker 🔐")
    user_password = input("Enter your password: ")
    result = check_password_strength(user_password)
    print(f"Password Strength: {result}")

if __name__ == "__main__":
    main()
