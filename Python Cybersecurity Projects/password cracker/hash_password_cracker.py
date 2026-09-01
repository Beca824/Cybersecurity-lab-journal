# Hash Password Cracker
# Python Cybersecurity Project 01 - Level 3
# Purpose: Simulate a dictionary attack against a password hash.
# The program hashes each password candidate from a wordlist
# and compares it with a target hash.

import hashlib
from pathlib import Path

target_hash = input("Enter the target SHA-256 hash: ")
wordlist_name = input("Enter the wordlist filename: ")
attempts = 0

print(Path(__file__).parent)

try:
    with open(Path(__file__).parent / wordlist_name, "r") as file:
        for password in file:
                password = password.strip()
                attempts += 1
                
                if hashlib.sha256(password.encode()).hexdigest() == target_hash:
                    print(f"Correct! Password: {password} (Attempt {attempts})")
                    break
                else:
                    print(f"Attempt {attempts}: {password} - Incorrect")
        else:
             print(f"Password not found. Tried {attempts} passwords.") 
except FileNotFoundError:
                    print("[ERROR] Wordlist file not found.")