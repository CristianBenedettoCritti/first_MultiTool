import requests
import os
import socket
import time

TOKEN_FILE = "tokens.txt"

def load_tokens():
    if not os.path.exists(TOKEN_FILE):
        open(TOKEN_FILE, "w").close()
        return []
    with open(TOKEN_FILE, "r") as f:
        return [line.strip() for line in f.readlines() if line.strip()]

def save_token(token):
    with open(TOKEN_FILE, "a") as f:
        f.write(f"{token}\n")

logo = """
\033[38;2;0;50;255m   __  ___  __  __   __  ______   ____      ______  ____   ____    __
\033[38;2;0;115;245m  /  |/  / / / / /  / / /_  __/  /  _/     /_  __/ / __ \ / __ \  / / 
\033[38;2;0;175;235m / /|_/ / / /_/ /  / /__ / /    _/ /        / /   / /_/ // /_/ / / /__
\033[38;2;0;225;215m/_/  /_/  \____/  /____//_/    /___/       /_/    \____/ \____/ /____/                                                            
"""

discord_config = {
    "message": "Hello World",
    "count": 1,
    "server_id": "Not Set",
    "channel_id": "Not Set"
}

while True:
    os.system("title MultiTool")
    os.system("cls")
    print(logo)
    print("[1] IP Lookup")
    print("[2] Port reader")
    print("[3] Discord Mass DM/Message")
    print("")
    x = input("Option: ")

    if x == "1":
        os.system("cls")
        print(logo)
        print("IP LOOKUP\n")
        ip = input("Enter IP: ")
        os.system("cls")
        try:
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
        except Exception as e:
            print(f"Error: {e}")
        input("Press enter to return...")

    if x == "2":
        os.system("cls")
        def scan_port():
            print(logo)
            target = input("Enter IP: ")
            port_range = input("Enter Port Range (e.g. 20-80): ")
            try:
                start_port, end_port = port_range.split("-")
                start_port = int(start_port)
                end_port = int(end_port)
            except ValueError:
                os.system("cls")
                print(logo)
                print("Invalid format. Please use 'start-end' (e.g., 20-80).")
                input("\nPress enter to return...")
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
            input("\nPress enter to return...")
        scan_port()

    if x == "3":
        while True:
            current_tokens = load_tokens()
            
            os.system("cls")
            print(logo)
            print("--- DISCORD CONFIGURATION MENU ---")
            print(f"[1] Add Token       (Loaded: {len(current_tokens)})")
            print(f"[2] Set Message     (Current: {discord_config['message']})")
            print(f"[3] Set Repeat Count(Current: {discord_config['count']})")
            print(f"[4] Set Server ID   (Current: {discord_config['server_id']})")
            print(f"[5] Set Channel ID  (Current: {discord_config['channel_id']})")
            print("")
            print("[6] \033[92mSTART SENDING\033[0m")
            print("[0] Back to Main Menu")
            print("----------------------------------")
            
            sub_choice = input("Select: ")

            if sub_choice == "1":
                print("\nType new tokens (type 'back' to finish):")
                while True:
                    t = input("Token > ")
                    if t.lower() == "back":
                        break
                    if t.strip():
                        save_token(t.strip())
                        print("Saved!")

            elif sub_choice == "2":
                discord_config["message"] = input("Enter new message: ")

            elif sub_choice == "3":
                try:
                    c = int(input("How many times to send? "))
                    discord_config["count"] = c
                except ValueError:
                    print("Please enter a valid number!")
                    time.sleep(1)

            elif sub_choice == "4":
                discord_config["server_id"] = input("Enter Server ID: ")

            elif sub_choice == "5":
                discord_config["channel_id"] = input("Enter Channel ID: ")

            elif sub_choice == "6":
                
                if not current_tokens or discord_config["channel_id"] == "Not Set":
                    print("\n\033[91mError: You need at least one token and a Channel ID!\033[0m")
                    time.sleep(2)
                else:
                    os.system("cls")
                    print(logo)
                    print(f"Starting process with {len(current_tokens)} tokens...")
                    print(f"Repeating {discord_config['count']} times per token.\n")
                    
                    for token_idx, token in enumerate(current_tokens):
                        print(f"--- Using Token {token_idx + 1} ---")
                        
                        for i in range(discord_config["count"]):
                            url = f"https://discord.com/api/v9/channels/{discord_config['channel_id']}/messages"
                            headers = {"Authorization": token, "Content-Type": "application/json"}
                            payload = {"content": discord_config["message"]}
                            
                            try:
                                r = requests.post(url, headers=headers, json=payload)
                                if r.status_code == 200:
                                    print(f"   [{i+1}/{discord_config['count']}] Sent: SUCCESS")
                                else:
                                    print(f"   [{i+1}/{discord_config['count']}] Failed: {r.status_code}")
                            except Exception as e:
                                print(f"   Error: {e}")
                            
                            time.sleep(1)
                        
                        print("")
                        
                    print("All done!")
                    input("Press enter to continue...")

            elif sub_choice == "0":
                break