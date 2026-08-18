# Hash Password Cracker
# Python Cybersecurity Project 01 - Level 3
# Purpose: Simulate a dictionary attack against a password hash.
# The program hashes each password candidate from a wordlist
# and compares it with a target hash.

import hashlib

password = "cyber123"
target_hash = hashlib.sha256(password.encode()).hexdigest()

print(f"Password: {password}")
print(f"Target hash: {target_hash}")