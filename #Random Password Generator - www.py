import random
import string

# A function to shuffle all the characters of a string
def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

# Main program starts here
# Generate one random uppercase letter
uppercaseLetter = random.choice(string.ascii_uppercase)

# Generate one random lowercase letter
lowercaseLetter = random.choice(string.ascii_lowercase)

# Generate one random digit
digit = random.choice(string.digits)

# Generate one random special character
specialChar = random.choice("!@#$%^&*()_+-=[]{};':\"\\|,.<>?/")

# Generate remaining characters to make the password 12 characters long
remaining_chars = ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{};':\"\\|,.<>?/", k=8))

# Combine all the characters
password = uppercaseLetter + lowercaseLetter + digit + specialChar + remaining_chars

# Shuffle the final password
password = shuffle(password)

# Output
print(password)
