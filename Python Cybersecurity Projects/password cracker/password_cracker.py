# Password Dictionary Cracker
# Python Cybersecurity Project 01 - Level 2
# Purpose: Simulate a dictionary attack using a predefined wordlist.
# The program tests each password candidate against a known test password
# and stops when a match is found.

from pathlib import Path

correct_password = "cyber123"
attempts = 0

wordlist_path = Path(__file__).parent / "wordlist.txt"

with open(wordlist_path, "r") as file:
    for password in file:
        password = password.strip()
        attempts = attempts + 1
        
        if password == correct_password:
            print(f"Attempt {attempts}: '{password}'  CORRECT!")
            print(f"\n[SUCCESS] Password found: {password}")
            print(f"Total attempts: {attempts}")
            break
        else:
            print(f"Attempt {attempts}: '{password}'  Incorrect")
    else:
        print(f"\n[FAILED] Password not found in wordlist")
        print(f"Total attempts: {attempts}")