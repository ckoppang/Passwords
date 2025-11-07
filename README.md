#  Password Manager

## Overview
This is a case study for the Johns Hopkins University's Applied GenAI course. Most of this file was given and this is the result of changing the code per suggested changes at the bottom. I changed the impl to include two new features 1/ modify the code to take the length input from the user for random password generation, and 2/ encrypt the files that store the master login passwords and the domain/application passwords.

I did not implement the second suggestion of encrypting just the password since doing that AND encrypting the entire file simply are not needed. The entire file is encrypted at rest. Ironically, the initial file contents are in the code, so it's not entirely a secret.

## Dependencies
 - Fernet is used for the encrypt / decrypt
 - load_dotenv is used to abstract where SECRET_KEY env variable is stored 
 - All other input file

## Setup
The key used for encryption is stored in an environment variable called SECRET_KEY. You need to either define the environment variable or create a .env file with with SECRET_KEY in it.

To create an initial SECRET_KEY run the following
'''
from cryptography.fernet import Fernet
print(Fernet.generate_key().decode())
'''

## Running
 - For initial login check the master_login.json decl in the code.
 - An unencrypted log.txt file is created in the same folder as the code is being run from.