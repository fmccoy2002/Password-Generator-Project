import random
import string
import base64

# Function to shuffle characters in a string
def shuffle(string):
    temp_list = list(string)
    random.shuffle(temp_list)
    return ''.join(temp_list)

# Function to suggest context based on password
def suggest_context(password):
    if len(password) >= 12 and any(c in "!@#$%^&*" for c in password):
        return "This password is perfect for securing banking or financial accounts!"
    elif len(password) >= 8 and any(c.isdigit() for c in password):
        return "This password is great for social media accounts!"
    else:
        return "This password is suitable for casual accounts or temporary use."

# List of motivational quotes
motivational_quotes = [
    "Security is not a product, but a process.",
    "Strong passwords protect great ideas.",
    "Every strong password is a step toward digital safety.",
    "Be the guardian of your digital fortress.",
    "A secure password is a key to peace of mind."
]

# Encode and Decode Password Functions
def encrypt_password(password):
    # Encode password as bytes, then base64 encode it
    return base64.b64encode(password.encode()).decode()

def decrypt_password(encoded_password):
    # Decode base64-encoded password back to original
    return base64.b64decode(encoded_password.encode()).decode()

# Collect user preferences
password_length = int(input("Enter the desired password length (minimum 8): "))
include_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
include_lowercase = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
include_digits = input("Include numbers? (y/n): ").strip().lower() == 'y'
include_special = input("Include special characters? (y/n): ").strip().lower() == 'y'

# Build the character pool based on preferences
character_pool = ""
if include_uppercase:
    character_pool += string.ascii_uppercase
if include_lowercase:
    character_pool += string.ascii_lowercase
if include_digits:
    character_pool += string.digits
if include_special:
    character_pool += "!@#$%^&*()_+-=[]{};':\"\\|,.<>?/"

if len(character_pool) == 0:
    print("No character types selected. Using all character types by default.")
    character_pool = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{};':\"\\|,.<>?/"

# Generate the password
password = ''.join(random.choices(character_pool, k=password_length))
password = shuffle(password)

# Encrypt and save the password
encrypted_password = encrypt_password(password)
with open("passwords.txt", "a") as file:
    file.write(encrypted_password + "\n")

# Display the password
print(f"\nGenerated password: {password}")
print(f"Encrypted password saved to passwords.txt.")

# Display the contextual hint
print("\nPassword Context Suggestion:")
print(suggest_context(password))

# Display a random motivational quote
print("\nMotivational Quote:")
print(random.choice(motivational_quotes))

# Optional: Decrypt and show password (for testing)
# Uncomment the lines below to test decryption
# print("\nDecrypted Password (for testing):")
# print(decrypt_password(encrypted_password))
