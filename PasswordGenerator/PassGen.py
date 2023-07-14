import secrets
import string
import os

# define the alphabet
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

alphabet = letters + digits + special_chars

# fix password length
pwd_length = 12

# generate a password string
pwd = ''
for i in range(pwd_length):
  pwd += ''.join(secrets.choice(alphabet))

print(pwd)

# generate password meeting constraints
while True:
  pwd = ''
  for i in range(pwd_length):
    pwd += ''.join(secrets.choice(alphabet))

  if (any(char in special_chars for char in pwd) and 
      sum(char in digits for char in pwd) >= 2):
          break

print(pwd)

# Prompt the user for the file name
file_name = input("Enter the desired file name (without extension): ")

# Check if the directory exists, if not, create it
directory = r"C:\Users\syarb\OneDrive\Desktop\Python Program\PasswordGenerator"
if not os.path.exists(directory):
    os.makedirs(directory)

# Store the password in the file
file_path = os.path.join(directory, file_name + ".txt")
with open(file_path, "w") as file:
    file.write(pwd)

print("Your file has been stored in the selected directory.")