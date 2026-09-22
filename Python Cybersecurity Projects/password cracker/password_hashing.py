# Password Hashing & Salting
# Python Cybersecurity Project 01 
# Purpose: Demonstrate how salts affect password hashing.

import hashlib
import secrets

password = "cyber123"

salt = secrets.token_hex(16)

salted_password = password + salt

hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()

print(f"Password: {password}")
print(f"Salt: {salt}")
print(f"Hash: {hashed_password}")
