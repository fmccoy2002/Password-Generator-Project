# from flask import Flask, render_template, request
# import random
# import string
# import requests

# app = Flask(__name__)

# # Function to shuffle characters in a string
# def shuffle(string):
#     temp_list = list(string)
#     random.shuffle(temp_list)
#     return ''.join(temp_list)

# # Function to generate a password
# def generate_password(length, include_uppercase, include_lowercase, include_digits, include_special):
#     character_pool = ""
#     if include_uppercase:
#         character_pool += string.ascii_uppercase
#     if include_lowercase:
#         character_pool += string.ascii_lowercase
#     if include_digits:
#         character_pool += string.digits
#     if include_special:
#         character_pool += "!@#$%^&*()_+-=[]{};':\"\\|,.<>?/"

#     if len(character_pool) == 0:
#         character_pool = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{};':\"\\|,.<>?/"

#     password = ''.join(random.choices(character_pool, k=length))
#     return shuffle(password)

# # Function to fetch common passwords
# def get_common_passwords():
#     url = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10k-most-common.txt"
#     response = requests.get(url)

#     if response.status_code == 200:
#         return response.text.splitlines()
#     else:
#         return []

# @app.route("/", methods=["GET", "POST"])
# def index():
#     password = None
#     context_suggestion = None
#     common_password_warning = None

#     if request.method == "POST":
#         # Retrieve form data
#         length = int(request.form.get("length", 12))
#         include_uppercase = "uppercase" in request.form
#         include_lowercase = "lowercase" in request.form
#         include_digits = "digits" in request.form
#         include_special = "special" in request.form

#         # Generate the password
#         password = generate_password(length, include_uppercase, include_lowercase, include_digits, include_special)

#         # Suggest context
#         if len(password) >= 12 and any(c in "!@#$%^&*" for c in password):
#             context_suggestion = "This password is perfect for securing banking or financial accounts!"
#         elif len(password) >= 8 and any(c.isdigit() for c in password):
#             context_suggestion = "This password is great for social media accounts!"
#         else:
#             context_suggestion = "This password is suitable for casual accounts or temporary use."

#         # Check against common passwords
#         try:
#             common_passwords = get_common_passwords()
#             if password in common_passwords:
#                 common_password_warning = "WARNING: This password is too common. Consider generating a new one."
#         except Exception as e:
#             common_password_warning = "Could not check common passwords due to an error."

#     return render_template("index.html", password=password, context_suggestion=context_suggestion, common_password_warning=common_password_warning)

# if __name__ == "__main__":
#     app.run(debug=True, port=5001)

import os
print("Current Working Directory:", os.getcwd())
print("Templates Folder Exists:", os.path.exists(os.path.join(os.getcwd(), 'templates')))
print("index.html Exists:", os.path.exists(os.path.join(os.getcwd(), 'templates', 'index.html')))