# Password Checker
# Python Cybersecurity Project 01
# Purpose: Simulate a basic password authentication system.
# The user gets three attempts to enter the correct password.

correct_password = "cyber123"
attempts = 0

while attempts < 3:
    password = input("Enter the password: ")
    attempts = attempts + 1
    
    if password == correct_password:
        print("Access granted!")
        break
    elif attempts == 1:
        print("Incorrect password, 2 tries left")
    elif attempts == 2:
        print("Incorrect password, 1 try left")
    elif attempts == 3:
        print("Access Denied")