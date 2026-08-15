from pathlib import Path

correct_password = "cyber123"
attempts = 0

wordlist_path = Path(__file__).parent / "wordlist.txt"

with open(wordlist_path, "r") as file:
    for password in file:
        password = password.strip()
        attempts = attempts + 1
        
        if attempts > 6:
            break
            
        if password == correct_password:
            print(f"Password found: {password}")
            break
        else:
            print("Incorrect password")
