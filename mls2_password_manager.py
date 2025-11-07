# -*- coding: utf-8 -*-
"""MLS2_Password_Manager.ipynb


# 🔐 SecureSphere Password Generator / Manager - Your Key to Unbreakable Protection! 🚀

SecureSphere Innovations is dedicated to providing top-tier protection against digital threats for businesses, financial institutions, and government agencies. One of the critical challenges faced by clients is securely managing a wide range of application and domain passwords.

To address this, SecureSphere Innovations is implementing a Secure Password Generator and Manager. This solution enables users to generate strong, random passwords and manage them along with it logs are also mantained of all the ongoing tasks. With user authentication integrated into the system, authorized personnel can safely add, update, retrieve, or delete passwords, ensuring that sensitive information remains secure and easily accessible when needed. The approach leverages modern security practices to ensure both ease of use and the highest level of protection against cyber threats.

# **Flow of the Password Generator / Manager**

### Problem Breakdown - Steps involved in create the Password Generator / Manager

1. **Default Setup**: Create default passwords and files for testing.

2. **Password Generation**: Build functions to generate random passwords based on length and specified criteria.

3. **Password Manager Functionalities**:
   - **Helper Methods**: Read/write passwords and logs.
   - **Add Password**: Add or auto-generate a 12-digit password for a domain.
   - **Retrieve Password**: View stored passwords.
   - **Update Password**: Update or auto-generate a password for a domain.
   - **Delete Password**: Remove a password for a domain.

4. **Main Function**: Centralize and navigate through all functionalities.

# Default Setup
"""

"""
Create a Python script that performs the following tasks:

1. **Import Libraries:**
   - Import the required libraries:
     - `os`: For interacting with the operating system (not used explicitly in the provided code, but part of the setup).
     - `json`: For handling JSON file operations, such as reading and writing.
     - `datetime`: Although it's imported, it's not used in the provided code, but it might be useful in other parts of the script for logging or time-related operations.

2. **Define File Locations and Names:**
   - Set file paths for three files:
     - `MASTER_LOGIN`: This file will store master login information, with the path set to `master_login.json`.
     - `PASSWORD_FILE`: This file will store application passwords, with the path set to `app_password.json`.
     - `LOG_FILE`: A log file for storing logs, with the path set to `log.txt` (although it's not used in the current logic).

3. **Create Dummy Data:**
   - Define two dictionaries with dummy data:
     - `master_login`: A dictionary that holds usernames as keys and their corresponding passwords as values. The provided example has the following data:
       ```python
       {"Jimmy": "robert@123", "Angela": "2009_Bonnet"}
       ```
     - `app_password`: A dictionary that maps usernames to a list of dictionaries. Each dictionary in the list contains `domain` and `pwd` (password for that domain). The provided example contains:
       ```python
       "Jimmy": [
           {"domain": "Facebook", "pwd": "JimmyGordan"},
           {"domain": "Instagram", "pwd": "B0atm@n"}
       ],
       "Angela": [
           {"domain": "Facebook", "pwd": "Angela009"},
           {"domain": "Instagram", "pwd": "Mikcy&Angela"}
       ]
       ```

4. **Write Data to Files:**
   - Use the `json.dump()` method to write the `master_login` and `app_password` data into their respective files:
     - Check if the files are not existing then only create the files.
     - Write the `master_login` data into the `MASTER_LOGIN` file (`master_login.json`).
     - Write the `app_password` data into the `PASSWORD_FILE` file (`app_password.json`).
     - Both JSON files should be formatted with an indentation of 4 spaces for readability.
"""

# Importing Libraries
import os, json
from datetime import datetime
import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv

# Read Fernet key from environment variable
load_dotenv()  # Loads variables from .env into environment

key = os.environ.get('SECRET_KEY')
if not key:
    raise RuntimeError("Encryption key not set in environment variable SECRET_KEY")
fernet = Fernet(key.encode())

# Initializing file locations and names
MASTER_LOGIN    =   'master_login.json'
PASSWORD_FILE   =   'app_password.json'
LOG_FILE        =   'log.txt'

# Dummy Data
# {"Username":"Password"}
master_login = {"Jimmy":"robert@123",
                "Angela":"2009_Bonnet"}

#  { "Username":[ {"domain":"", "pwd":"" },
#                 {"domain":"", "pwd":"" },... ] }
app_password = {
    "Jimmy": [
        {"domain": "Facebook", "pwd": "JimmyGordan"},
        {"domain": "Instagram", "pwd": "B0atm@n"}
    ],
    "Angela": [
        {"domain": "Facebook", "pwd": "Angela009"},
        {"domain": "Instagram", "pwd": "Mikcy&Angela"},
    ]
}

# Helper functions for encrypted file access
def write_encrypted_json(file_path, data):
    with open(file_path, 'wb') as file:
        file.write(fernet.encrypt(json.dumps(data, indent=4).encode()))

def read_encrypted_json(file_path):
    if not os.path.exists(file_path):
        return {}
    with open(file_path, 'rb') as file:
        encrypted = file.read()
        try:
            decrypted = fernet.decrypt(encrypted)
            return json.loads(decrypted.decode())
        except Exception:
            return {}

# writing the dummy data into the files
if not os.path.exists(MASTER_LOGIN):
    write_encrypted_json(MASTER_LOGIN, master_login)
    print(f"{MASTER_LOGIN} created and data written.")

if not os.path.exists(PASSWORD_FILE):
    write_encrypted_json(PASSWORD_FILE, app_password)
    print(f"{PASSWORD_FILE} created and data written.")

"""# Random password

* Password Length : The default length of the password is set to `12`, but it can be adjusted by passing a different value to the length parameter.
---
* Character Sets:

  * `string.ascii_lowercase` : Includes all lowercase `(a-z)`.
  * `string.ascii_upp
  ercase` : Includes all lowercase `(A-Z)`.
  *  `string.digits` : Includes all digits `(0-9)`.
  * `string.punctuation` : Includes special characters like `!@#$%^&*()-_=+` and others.
---
* `secrets.choice()` : This function is used to select a random character from the allowed character set securely, ensuring cryptographic strength.
"""

""" PROMPT
Write a Python function getting_equal_length(num) that divides a given number num into four nearly equal parts. The function should:

1. Calculate the integer division of num by 4 (quotient = num // 4).
2. Calculate the remainder when num is divided by 4 (remainder = num % 4).
3. Create a list result that contains the quotient repeated 4 times.
4. Distribute the remainder among the first few elements of the list (add 1 to the first remainder elements).
5. Return the resulting list where the values represent the closest possible split of num into four nearly equal parts.

For example:
- If num = 10, the function should return [3, 3, 2, 2].
- If num = 11, the function should return [3, 3, 3, 2].
- If num = 12, the function should return [3, 3, 3, 3].
"""

def getting_equal_length(num):
    # Divide the number by 4 using integer division
    quotient = num // 4
    remainder = num % 4
    # Create a list with the quotient repeated 4 times
    result = [quotient] * 4
    # Distribute the remainder among the first few elements
    for i in range(remainder):
        result[i] += 1
    return result

getting_equal_length(2)

""" PROMPT
Write a Python function `generate_secure_password(length=12)` that generates a secure and random password based on a specified length. The password should meet the following criteria:

1. Use a mix of:
   - Lowercase letters (`string.ascii_lowercase`)
   - Uppercase letters (`string.ascii_uppercase`)
   - Digits (`string.digits`)
   - Special characters (`string.punctuation`)

2. Distribute the `length` of the password among these four character categories as evenly as possible. This distribution should be determined by calling the previously created function `getting_equal_length(length)`, which divides the length into four parts. Store the result in a variable named `distribution`.

3. The `distribution` list should contain:
   - The first part represents the number of lowercase letters.
   - The second part represents the number of uppercase letters.
   - The third part represents the number of digits.
   - The fourth part represents the number of special characters.

4. Generate a random character for each category using `secrets.choice` and the corresponding set of characters (lowercase, uppercase, digits, and punctuation).

5. Shuffle the resulting list of characters using `secrets.SystemRandom().shuffle()` to ensure the password is randomized.

6. Return the generated password as a string.

For example:
- If `length = 12`, the function might return something like `"aB1$gV3z&hQ9"`.
- If `length = 16`, the function might return something like `"pX2m!zT8#qWjC7D4"`.
"""


import secrets
import string

def generate_secure_password(length=12):
    distribution = getting_equal_length(length)

    password = []

    password += [secrets.choice(string.ascii_lowercase) for _ in range(distribution[0])]
    password += [secrets.choice(string.ascii_uppercase) for _ in range(distribution[1])]
    password += [secrets.choice(string.digits) for _ in range(distribution[2])]
    password += [secrets.choice(string.punctuation) for _ in range(distribution[3])]


    # Shuffling the password
    secrets.SystemRandom().shuffle(password)
    return ''.join(password)

"""# Password Manager

### 0. Helper Methods
"""

""" PROMPT
Write a Python script that implements three functions for managing passwords and logging:

1. **`read_passwords()`**:
   - Check if a file, referred to by `PASSWORD_FILE`, exists.
   - If the file exists, open the file in read mode and load its contents as JSON.
   - Return the loaded data as a dictionary.
   - If the file does not exist, return an empty dictionary.

2. **`write_passwords(data)`**:
   - Take a dictionary `data` as input.
   - Open the file referred to by `PASSWORD_FILE` in write mode.
   - Write the dictionary `data` to the file in JSON format with an indentation of 4 spaces for readability.

3. **`log_update(message)`**:
   - Open a log file, referred to by `LOG_FILE`, in append mode.
   - Write the `message` to the log file, prepended with the current date and time, formatted as `"{datetime.now()} - {message}"`.

Do not add any additional functionality or changes to the code.
"""

# Function to read the stored passwords from the file
def read_passwords():
    return read_encrypted_json(PASSWORD_FILE)

def write_passwords(data):
    write_encrypted_json(PASSWORD_FILE, data)

# Function to log updates to the password log
def log_update(message):
    with open(LOG_FILE, 'a+') as log_file:
        log_file.write(f"{datetime.now()} - {message}\n")

"""### 1. Add Password"""

""" PROMPT
Write a Python function `add_password(uid)` that adds a password entry for a user. The function should perform the following steps:

1. **Read stored passwords**: Call the previously defined `read_passwords()` function to load the existing passwords.

2. **Prompt the user**: Display a header with the title "Add Password" and prompt the user to input the domain name and password for a particular domain. Include a note that if the user wishes to generate a random password, they can leave the password field blank.

3. **Generate a random password**: If the user does not provide a password (i.e., leaves it blank), use the previously defined `generate_secure_password()` function to generate a random password.

4. **Check user existence**: Verify if the user (identified by `uid`) exists in the `app_password` dictionary. If not, initialize an empty list for that user.

5. **Create a new password entry**: Create a dictionary with the domain and password, and append this entry to the user's password list in the `app_password` dictionary.

6. **Write the updated data**: Call the previously defined `write_passwords(app_password)` function to save the updated list of passwords back to the file.

7. **Log the update**: Call the `log_update()` function to log the action, noting that a password for the specified domain has been added for the given user.

8. **Display success message**: Print a decorative success message indicating that the password for the specified domain has been successfully added.

Do not modify the provided structure or logic of the code in any way.
"""

def add_password(uid):
    # Read the stored passwords from the file
    app_password = read_passwords()

    # Prompt user to enter domain and password
    print("="*40)
    print(f"{'Add Password'.center(40)}")
    print("="*40)

    domain = input("Enter the domain name: ")
    print(f"<======  If you wish to generate a random password, leave the password field as blank. ======>")
    password = input("Enter the password for the domain: ")

    # Generating a random password if the user has not provided the password
    if password == "":
        try:
            length = int(input("Enter desired password length (default 12): ") or 12)
        except ValueError:
            length = 12
        password = generate_secure_password(length)

    # Check if the user exists in app_password; if not, initialize an empty list for them
    if uid not in app_password:
        app_password[uid] = []

    # Create a new password entry
    new_entry = { "domain": domain, "pwd": password }

    # Append the new entry to the user's password list
    app_password[uid].append(new_entry)

    # Write the updated password list back to the file
    write_passwords(app_password)

    # Log the action for tracking purposes
    log_update(f"Added password for {domain} under user {uid}")

    # Print success message with a decorative format
    print("*"*40)
    print(f"Password for {domain} has been added successfully.")
    print("*"*40)

"""### 2. Retrieve Password"""

""" PROMPT
Write a Python function `retrieve_password(uid)` that allows a user to retrieve stored passwords. The function should perform the following steps:

1. **Read stored passwords**: Call the previously defined `read_passwords()` function to load the stored passwords.

2. **Check user existence**: Check if the user (identified by `uid`) exists in the `app_password` dictionary and if they have stored passwords.

3. **Display stored domains**:
   - If the user has passwords, print a decorative title "Stored Passwords" centered and then list all the domains for which passwords are stored for that user.
   - Use a numbered list to display the domains (e.g., 1. domain1.com, 2. domain2.com, etc.).

4. **Allow user selection**:
   - Prompt the user to input a number corresponding to the domain they want to view the password for.
   - Validate that the input is a valid integer and within the correct range of listed options.

5. **Display the selected password**:
   - If the input is valid, display the password for the selected domain with a decorative format.
   - Log this action by calling the `log_update()` function, noting the domain from which the password was retrieved.

6. **Handle invalid inputs**:
   - If the user inputs an invalid number (out of range or non-integer), print an error message prompting the user to select a valid option.

7. **Handle missing data**:
   - If no passwords are found or the user does not exist in the `app_password` dictionary, print an appropriate error message indicating that no passwords are stored for the user or the user was not found.

Do not modify the provided structure or logic of the code in any way.
"""


def retrieve_password(uid):
    # Read the stored passwords from the file
    app_password = read_passwords()

    # Check if the user exists and has stored passwords
    if uid in app_password and app_password[uid]:
        print("="*40)
        print(f"{'Stored Passwords'.center(40)}")  # Title centered
        print("="*40)

        # Enumerate through the list of stored passwords and display the domains
        for index, entry in enumerate(app_password[uid], 1):
            print(f"{index}. {entry['domain']}")  # List the domain name (website)

        # Allow the user to select an option to view a specific password
        try:
            choice = int(input("\nEnter the option number to display the password: "))

            # Validate the user's choice
            if 0 < choice <= len(app_password[uid]):
                selected_entry = app_password[uid][choice - 1]

                # Display the selected password details with decorative formatting
                print("*"*40)
                decrypted_pwd = selected_entry['pwd']
                print(f"Password for {selected_entry['domain']} ==> {decrypted_pwd}")
                print("*"*40)
                # Log the password retrieval
                log_update(f"Retrieved password for {selected_entry['domain']} under user {uid}")

            else:
                # Invalid option if the choice is out of range
                print("\n[!] Invalid option selected. Please choose a valid number.\n")

        except ValueError:
            # Error message if the user does not input a valid integer
            print("\n[!] Please enter a valid number.\n")

    else:
        # If no passwords are stored or user is not found
        print("\n[!] No passwords stored or user not found.\n")

"""### 3. Update Password"""

""" PROMPT
Write a Python function `update_password(uid)` that allows a user to update the password for a specific domain. The function should perform the following steps:

1. **Read stored passwords**: Call the previously defined `read_passwords()` function to load the stored passwords.

2. **Check user existence**: Check if the user (identified by `uid`) exists in the `app_password` dictionary and if they have stored passwords.

3. **Display stored domains**:
   - If the user has passwords, print a decorative title "Stored Passwords" centered and then list all the domains for which passwords are stored for that user.
   - Use a numbered list to display the domains (e.g., 1. domain1.com, 2. domain2.com, etc.).

4. **Allow user selection**:
   - Prompt the user to input a number corresponding to the domain for which they want to update the password.
   - Validate that the input is a valid integer and within the correct range of listed options.

5. **Prompt for a new password**:
   - If the input is valid, prompt the user to enter a new password for the selected domain.
   - If the user leaves the password field blank, generate a random password using the previously defined `generate_secure_password()` function.

6. **Write the updated data**:
   - Save the updated password list back to the file by calling the `write_passwords()` function.

7. **Log the update**:
   - Call the `log_update()` function to log the password update action, noting the domain for which the password was updated.

8. **Provide feedback**:
   - Print a success message indicating the password has been successfully updated for the selected domain.

9. **Handle invalid inputs**:
   - If the user inputs an invalid number (out of range or non-integer), print an error message prompting the user to select a valid option.

10. **Handle missing data**:
    - If no passwords are found or the user does not exist in the `app_password` dictionary, print an appropriate error message indicating that no passwords are stored for the user or the user was not found.

Do not modify the provided structure or logic of the code in any way.
"""


def update_password(uid):
    # Read the stored passwords from the file
    app_password = read_passwords()

    # Check if the user exists and has stored passwords
    if uid in app_password and app_password[uid]:
        print("="*40)
        print(f"{'Stored Passwords'.center(40)}")  # Title centered
        print("="*40)

        # Enumerate through the list of stored passwords and display the domains
        for index, entry in enumerate(app_password[uid], 1):
            print(f"{index}. {entry['domain']}")  # Display domain name

        # Allow the user to select an option to update a specific password
        try:
            choice = int(input("\nEnter the option number to update the password: "))

            # Validate if the choice is within the valid range
            if 0 < choice <= len(app_password[uid]):
                selected_entry = app_password[uid][choice - 1]

                # Prompt the user for the new password
                print(f"<======  If you wish to generate a random password, leave the password field as blank. ======>")
                new_password = input(f"Enter the new password for {selected_entry['domain']}: ")

                # Generating a random password if the user has not provided the password and updating it
                if new_password == "":
                    try:
                        length = int(input("Enter desired password length (default 12): ") or 12)
                    except ValueError:
                        length = 12
                    selected_entry["pwd"] = generate_secure_password(length)
                else:
                    selected_entry["pwd"] = new_password

                # Write the updated passwords back to the file
                write_passwords(app_password)

                # Log the password update
                log_update(f"Updated password for {selected_entry['domain']} under user {uid}")

                # Provide success feedback to the user
                print("*"*40)
                print(f"Password for {selected_entry['domain']} updated successfully.")
                print("*"*40)

            else:
                # Handle invalid selection
                print("\n[!] Invalid option selected. Please choose a valid number.\n")

        except ValueError:
            # Handle non-integer input
            print("\n[!] Please enter a valid number.\n")

    else:
        # If no passwords are stored or user is not found
        print("\n[!] No passwords stored or user not found.\n")

"""### 4. Delete Password"""

""" PROMPT

Write a Python function `delete_password(uid)` that allows a user to delete a specific password entry. The function should perform the following steps:

1. **Read stored passwords**: Call the previously defined `read_passwords()` function to load the stored passwords.

2. **Check user existence**: Verify if the user (identified by `uid`) exists in the `app_password` dictionary and if they have stored passwords.

3. **Display stored domains**:
   - If the user has passwords, print a decorative title "Stored Passwords" centered and then list all the domains for which passwords are stored for that user.
   - Use a numbered list to display the domains (e.g., 1. domain1.com, 2. domain2.com, etc.).

4. **Allow user selection**:
   - Prompt the user to input a number corresponding to the domain for which they want to delete the password.
   - Validate that the input is a valid integer and within the correct range of listed options.

5. **Delete the selected password**:
   - If the input is valid, delete the selected password entry from the list using the `pop()` method.

6. **Write the updated data**:
   - Save the updated password list back to the file by calling the `write_passwords()` function.

7. **Log the deletion**:
   - Call the `log_update()` function to log the password deletion action, noting the domain for which the password was deleted.
   - Also log the full credentials (user, domain, and password) that were deleted.

8. **Provide feedback**:
   - Print a success message indicating the password has been successfully deleted for the selected domain.

9. **Handle invalid inputs**:
   - If the user inputs an invalid number (out of range or non-integer), print an error message prompting the user to select a valid option.

10. **Handle missing data**:
    - If no passwords are found or the user does not exist in the `app_password` dictionary, print an appropriate error message indicating that no passwords are stored for the user or the user was not found.

Do not modify the provided structure or logic of the code in any way.
"""


def delete_password(uid):
    # Read the stored passwords from the file
    app_password = read_passwords()

    # Check if the user exists and has stored passwords
    if uid in app_password and app_password[uid]:
        print("=" * 40)
        print(f"{'Stored Passwords'.center(40)}")
        print("=" * 40)

        # Enumerate through the list of stored passwords and display the domains
        for index, entry in enumerate(app_password[uid], 1):
            print(f"{index}. {entry['domain']}")

        try:
            choice = int(input("\nEnter the option number to delete the password: "))
            if 0 < choice <= len(app_password[uid]):
                deleted_entry = app_password[uid].pop(choice - 1)  # Delete the entry

                write_passwords(app_password)  # Update the password file

                log_update(f"Deleted password for {deleted_entry['domain']} under user {uid}")
                log_update(f"Deleted credentials - user: {uid}, domain: {deleted_entry['domain']}, password: {deleted_entry['pwd']} ")

                print("*" * 40)
                print(f"Password for {deleted_entry['domain']} deleted successfully.")
                print("*" * 40)

            else:
                print("\n[!] Invalid option selected. Please choose a valid number.\n")

        except ValueError:
            print("\n[!] Please enter a valid number.\n")
    else:
        print("\n[!] No passwords stored or user not found.\n")

"""### 5. Main Function"""

""" PROMPT
Write a Python function `main()` that simulates the operation of a Password Manager. The function should perform the following tasks:

1. **Welcome Header**: Print a decorative header with the message "Welcome to the Password Manager", centered, and enclosed within lines of "=" symbols.

2. **User Login**:
   - Prompt the user to input their UID.
   - If the UID does not exist in the `master_login` dictionary, display an error message ("User not found") and prompt for the UID again.
   - Prompt the user to input their password.
   - If the password does not match the one in the `master_login` dictionary for the given UID, display an error message ("Password mismatch") and prompt for the password again.
   - Log the successful login using the `log_update()` function.
   - Once logged in, display a success message, "Login successful - Welcome {uid}" in a stylized format.

3. **Menu for Actions**:
   - After successful login, present a menu with the following options:
     - 1. Add Password
     - 2. Retrieve Password
     - 3. Update Password
     - 4. Delete Password
     - 9. Exit
   - Based on the user’s choice, call the corresponding function (`add_password()`, `retrieve_password()`, `update_password()`, `delete_password()`) with the UID as a parameter.
   - If the user selects "9", print a farewell message and break the loop.

4. **Invalid Input Handling**:
   - If the user selects an invalid option, display an error message and prompt them to try again.

5. **Exit and End Message**:
   - Once the user selects "9", print a thank you message, "Thank you for using the Password Manager!", centered within lines of "=" symbols.
   - Break the loop to exit after finishing tasks.

6. **Entry Point**:
   - Use `if __name__ == "__main__":` to call the `main()` function.

Do not modify the provided structure or logic of the code in any way.
"""

def main():

    master_login = read_encrypted_json(MASTER_LOGIN)
    PASSWORD_FILE_DATA = read_encrypted_json(PASSWORD_FILE)

    while True:
        # Create a more visually appealing header
        print("="*40)
        print(f"{'Welcome to the Password Manager'.center(40)}")
        print("="*40)

        # User login
        uid = input("Enter your UID: ")
        if uid not in master_login:
            print("\n[!] User not found.\n")
            continue

        pss = input("Enter your password: ")
        if master_login[uid] != pss:
            print("\n[!] Password mismatch.\n")
            continue

        # updating the log for an user login
        log_update(f"User {uid} has logged-in")

        # Success message with stylized heading
        print("*"*40)
        print(f"{f'Login successful - Welcome {uid}'.center(40)}")
        print("*"*40)

        # Menu for actions
        while True:
            print("\nSelect an option:")
            print("+"*40)
            print("1. Add Password")
            print("2. Retrieve Password")
            print("3. Update Password")
            print("4. Delete Password")
            print("9. Exit")
            print("+"*40)

            choice = input("Choose an option: ")

            if choice == "1":
                add_password(uid)
            elif choice == "2":
                retrieve_password(uid)
            elif choice == "3":
                update_password(uid)
            elif choice == "4":
                delete_password(uid)
            elif choice == "9":
                print(f"\n[!] Exiting the Password Manager. Stay safe! - {uid}")
                break
            else:
                print("\n[!] Invalid option. Please try again.\n")

        # End message
        print("="*40)
        print(f"{'Thank you for using the Password Manager!'.center(40)}")
        print("="*40)
        break  # Break the while loop to exit after finishing tasks.

if __name__ == "__main__":
    main()

"""**Further Improvements**
Here is the rectified version of your sentence:

1. Modify the code to take the length input from the user for random password generation.
2. Encrypt the passwords before storing them in the password file.
3. Encrypt the files that store the master login passwords and the domain/application passwords.
4. Develop a UI using Streamlit or Flask, then host it for broader access.


"""

