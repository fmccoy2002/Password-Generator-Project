# Password Generator Final Project
 Helps me make new passwords and helps me remember them 


# Password Project

---

## Big Idea / Goal

### Why Did We Do This?
The Password Project was designed to help users easily generate **secure and unique passwords** for different purposes while also providing guidance on how to use them effectively. It addresses the common challenge of creating strong passwords, ensuring they are both random and relevant for the user’s needs. 

The tool also includes encryption for secure storage, motivational feedback, and a check against commonly used weak passwords. The ultimate goal is to make password management accessible, reliable, and even enjoyable.

---

## User Instructions

### Installation
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-repo/password-project.git
   cd password-project

Ensure Python 3.x is installed on your system.

Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Run the tool:

bash
Copy code
python password_tool.py
How to Use
Run the script and follow the prompts to:
Enter the desired password length (minimum 8 characters).
Choose the character types you want to include: uppercase letters, lowercase letters, digits, and special characters.
Receive your secure, unique password.
View contextual suggestions for the password’s use.
Save the password securely in an encrypted format.
(Optional) Test decryption to retrieve your stored password.
Implementation Details
Key Features
Password Generation:

Creates secure passwords with a mix of user-specified character types.
Ensures randomness for optimal security.
Contextual Suggestions:

Provides tips on where and how to use the generated password based on its strength.
Motivational Feedback:

Displays security-related motivational quotes to inspire good password habits.
Encryption:

Uses Base64 encoding to securely store passwords in an encrypted format.
Common Password Check:

Scrapes the NordPass website to check generated passwords against commonly used weak passwords.
Customization:

Allows users to specify password length and character preferences.
How It Works
The project uses several Python functions and libraries to ensure functionality:

shuffle(string): Randomizes the order of characters in a string.
suggest_context(password): Provides context for the password's potential use.
encrypt_password(password): Encrypts the password for secure storage.
decrypt_password(encoded_password): Decodes encrypted passwords when needed.
get_common_passwords(): Scrapes the NordPass website to fetch a list of weak passwords.
Limitations
API Issue: Integration with the OpenAI API for advanced password analysis was attempted but faced a "module not found" error. Resolving this issue is a priority for future updates.
Results
Screenshots
Password Generation

Encrypted Password Storage

Motivational Feedback

Key Outcomes
Generated secure passwords that are tailored to user needs.
Stored passwords securely with encryption to protect sensitive data.
Enhanced user experience with motivational feedback and contextual recommendations.
Project Evolution
Timeline
Initial Concept: Focused solely on generating strong passwords.
First Updates: Added contextual recommendations and motivational feedback.
Midway Improvements: Implemented encryption to securely store passwords.
Final Version: Integrated common password checks and improved user engagement.
Next Steps
Fix API Dependency: Resolve the OpenAI module issue to add advanced analysis features.
Improve Encryption: Implement more robust encryption methods beyond Base64.
Develop a GUI: Build a user-friendly graphical interface to make the tool more accessible.
Attribution
Libraries Used
random and string: For generating and shuffling passwords.
base64: For encrypting and decrypting passwords.
requests and BeautifulSoup: For scraping the NordPass website.
External Resources
NordPass Common Passwords
Python Official Documentation
