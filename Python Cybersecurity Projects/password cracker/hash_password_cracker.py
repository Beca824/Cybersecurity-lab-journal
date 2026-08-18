# Hash Password Cracker
# Python Cybersecurity Project 01 - Level 3
# Purpose: Simulate a dictionary attack against a password hash.
# The program hashes each password candidate from a wordlist
# and compares it with a target hash.

import hashlib
from pathlib import Path

target_hash = "5fc458731c2a36c7c1a96099158d709ed7209737617592202b54b1b30effcce8"
attempts = 0

with open(Path(__file__).parent / "wordlist.txt", "r") as file:
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