import requests
import os
import json

logo = """
\033[38;2;0;50;255m   __  ___  __  __   __  ______   ____      ______  ____   ____    __
\033[38;2;0;115;245m  /  |/  / / / / /  / / /_  __/  /  _/     /_  __/ / __ \ / __ \  / / 
\033[38;2;0;175;235m / /|_/ / / /_/ /  / /__ / /    _/ /        / /   / /_/ // /_/ / / /__
\033[38;2;0;225;215m/_/  /_/  \____/  /____//_/    /___/       /_/    \____/ \____/ /____/                                                            
"""

while True:
    os.system("title MultiTool")
    os.system("cls")
    print(logo)
    print("[1] IP Lookup")
    print("[2] Webhook")
    print("[3] token")
    print("")
    x = input("Option: ")

    if x == "1":
        os.system("cls")
        print("IP LOOKUP\n")
        ip = input("Enter IP: ")
        os.system("cls")
        r = requests.get(f"http://ip-api.com/json/{ip}")
        data = r.json()
        if data.get("status") == "success":
            print(f"Results for {data['query']}\n")
            print(f"Country: {data['country']}")
            print(f"City: {data['city']}")
            print(f"Region: {data['region']}")
            print(f"TimeZone: {data['timezone']}")
            print("")
        else:
            print(f"Failed to load: {ip}\n")
    pause = input("Press enter to return...")

    if x == "2":
        os.system("cls")
        webhook = input("Enter Webhook: ")

    if x == "3":
        os.system("cls")
        token = input("Enter Token: ")