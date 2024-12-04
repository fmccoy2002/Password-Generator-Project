import random
import string

# Function to shuffle characters in a string
def shuffle(string):
    temp_list = list(string)
    random.shuffle(temp_list)
    return ''.join(temp_list)

# Function to generate a sentence for a character
def generate_sentence(character):
    sentences = {
    'A': "A is for ambition, the spark of success.",
    'B': "B is for bravery, the courage to try.",
    'C': "C is for curiosity, the key to learning.",
    'D': "D is for determination, the drive to achieve.",
    'E': "E is for energy, the fuel of action.",
    'F': "F is for friendship, the bond that supports.",
    'G': "G is for growth, the journey to betterment.",
    'H': "H is for hope, the light in dark times.",
    'I': "I is for imagination, the seed of innovation.",
    'J': "J is for joy, the essence of living.",
    'K': "K is for kindness, the gift of the heart.",
    'L': "L is for love, the foundation of connection.",
    'M': "M is for mindfulness, the key to presence.",
    'N': "N is for knowledge, the power to transform.",
    'O': "O is for opportunity, the door to possibility.",
    'P': "P is for persistence, the strength to endure.",
    'Q': "Q is for quest, the pursuit of purpose.",
    'R': "R is for resilience, the power to recover.",
    'S': "S is for strength, the backbone of effort.",
    'T': "T is for trust, the glue of relationships.",
    'U': "U is for uniqueness, the quality that makes you special.",
    'V': "V is for vision, the map to your dreams.",
    'W': "W is for wisdom, the treasure of experience.",
    'X': "X is for excellence, the standard to strive for.",
    'Y': "Y is for yearning, the desire to grow.",
    'Z': "Z is for zeal, the passion that drives you forward.",
    '0': "Zero is the start, the potential of everything.",
    '1': "One step at a time leads to great journeys.",
    '2': "Two minds together create boundless ideas.",
    '3': "Three is the charm, the magic of balance.",
    '4': "Four stands for foundation, the strength to build.",
    '5': "Five fingers work together to grasp greatness.",
    '6': "Six is for harmony, the balance of life’s flow.",
    '7': "Seven signifies luck, the spark of serendipity.",
    '8': "Eight is infinite, the loop of endless possibility.",
    '9': "Nine is for completion, the beauty of wholeness.",
    '10': "Ten marks perfection, the essence of mastery.",
    '!': "Exclamation marks add excitement to life!",
    '@': "The at symbol connects us all online.",
    '#': "The hashtag unites ideas and communities.",
    '$': "The dollar sign represents value and exchange.",
    '%': "Percentages show progress and comparison.",
    '^': "The caret lifts ideas higher in importance.",
    '&': "The ampersand binds words and concepts together.",
    '*': "Asterisks highlight the exceptional.",
    '(': "Open parentheses invite thoughts to expand.",
    ')': "Closed parentheses signify completion and clarity.",
    '_': "The underscore bridges words and meaning.",
    '+': "The plus sign adds positivity to equations.",
    '-': "The dash connects ideas seamlessly.",
    '=': "Equals stands for fairness and balance.",
    '[': "Open brackets hold details within.",
    ']': "Closed brackets wrap up structure.",
    '{': "Curly braces group creativity together.",
    '}': "Curly braces close the loop of innovation.",
    ';': "Semicolons link related thoughts elegantly.",
    "'": "Apostrophes show ownership and belonging.",
    ':': "Colons introduce insights and explanations.",
    '"': "Quotation marks bring words to life.",
    '\\': "Backslashes show escape and direction.",
    '|': "The pipe divides and redirects ideas.",
    ',': "Commas give pauses for reflection.",
    '.': "Periods end sentences with confidence.",
    '<': "Less than leads to deeper comparisons.",
    '>': "Greater than inspires ambitious goals.",
    '?': "Question marks spark curiosity and inquiry.",
    '/': "Slashes separate paths and possibilities."
    }
    # Return a predefined sentence or a default message
    return sentences.get(character, f"No sentence defined for '{character}'.")

# Main program starts here
# Generate a secure password
uppercase_letter = random.choice(string.ascii_uppercase)
lowercase_letter = random.choice(string.ascii_lowercase)
digit = random.choice(string.digits)
special_char = random.choice("!@#$%^&*()_+-=[]{};':\"\\|,.<>?/")

# Generate additional random characters
remaining_chars = ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{};':\"\\|,.<>?/", k=8))
password = uppercase_letter + lowercase_letter + digit + special_char + remaining_chars
password = shuffle(password)

# Display the password
print(f"Generated password: {password}")

# Generate sentences for each character
print("\nGenerated sentences:")
for char in password:
    sentence = generate_sentence(char)
    print(f"{char}: {sentence}")

