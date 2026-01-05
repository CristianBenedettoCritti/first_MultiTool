import requests
import os
import json
import socket

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
    print("[2] Port reader")
    print("[3] token")
    print("")
    x = input("Option: ")

    if x == "1":
        os.system("cls")
        print(logo)
        print("IP LOOKUP\n")
        ip = input("Enter IP: ")
        os.system("cls")
        r = requests.get(f"http://ip-api.com/json/{ip}")
        data = r.json()
        if data.get("status") == "success":
            print(logo)
            print(f"Results for {data['query']}\n")
            print(f" Country: {data['country']}")
            print(f"  Region: {data['regionName']}")
            print(f"    City: {data['city']}")
            print(f"     Zip: {data['zip']}")
            print(f"Location: {data['lat']}, {data['lon']}")
            print(f"TimeZone: {data['timezone']}")
            print("")
        else:
            print(logo)
            print(f"Failed to load: {ip}\n")
        pause = input("Press enter to return...")

    if x == "2":
        os.system("cls")
        def scan_port():
            print(logo)
            target = input("Enter IP: ")
            port_range = input("Enter Port Range: ")
            try:
                start_port, end_port = port_range.split("-")
                start_port = int(start_port)
                end_port = int(end_port)
            except ValueError:
                print("Invalid format. Please use 'start-end' (e.g., 20-80).")
                return
            os.system("cls")
            print(logo)
            print(f"Scanning {target} from port {start_port} to {end_port}...\n")

            for port in range(start_port, end_port + 1):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.05)
                result = s.connect_ex((target, port))
                if result == 0:
                    print(f"Port {port}: OPEN")
                    s.close()
            pause = input("\nPress enter to return...")
        scan_port()

    if x == "3":
        os.system("cls")
        print(logo)
        token = input("Enter Token: ")