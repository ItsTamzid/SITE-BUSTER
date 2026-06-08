import requests
import os 
import sys
import socket
import time

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
BOLD = "\033[1m"
RESET = "\033[0m"

BANNER = f"""
{RED}{BOLD} ____ ___ _____ _____ ____  _   _ ____ _____ _____ ____  
/ ___|_ _|_   _| ____| __ )| | | / ___|_   _| ____|  _ \\ 
\\___ \\| |  | | |  _| |  _ \\| | | \\___ \\ | | |  _| | |_) |
 ___) | |  | | | |___| |_) | |_| |___) || | | |___|  _ < 
|____/___| |_| |_____|____/ \\___/|____/ |_| |_____|_| \\_\\
{RESET}{YELLOW}       >> Advanced Multi-URL Recon Weapon <<
{RESET}"""

def get_ip_address(domain_list):
    for domain in domain_list:
        try:
            # डोमेन से http/https हटाना ताकि IP मिल सके
            clean_domain = domain.replace("http://", "").replace("https://", "").split('/')[0]
            ip_address = socket.gethostbyname(clean_domain)
            print(f"      {YELLOW}{domain}{RESET}  {BOLD}-->{RESET}  {GREEN}{ip_address}{RESET}")
        except socket.gaierror:
            print(f"      {YELLOW}{domain}{RESET}  {BOLD}-->{RESET}  {RED}Could not resolve domain.{RESET}")

def SITE_BUSTER(url_list):
    print(f"             {BLUE}{BOLD}=== SITE-BUSTER ACTIVE ==={RESET}\n")
    for i in url_list:
        try:
            respons = requests.get(i, timeout=5)
            status = respons.status_code
            if status == 200: print(f"    {GREEN}[SUCCESS] {i} - Found! status: {status}{RESET}")
            elif status in [301, 302]: print(f"    {BLUE}[REDIRECT] {i} - Site moved! status: {status}{RESET}")
            elif status == 404: print(f"    {YELLOW}[FAILED] {i} - Not found! status: {status}{RESET}")
            else: print(f"    {RED}[STATUS] {i} - Status code: {status}{RESET}")
        except requests.exceptions.RequestException:
            print(f"    {RED}{BOLD}[ERROR] {i} - Connection failed!{RESET}")

def main_menu():
    while True:
        os.system('clear')
        print(BANNER)
        print(f"      • {CYAN}1){RESET} {GREEN}GET IP-ADDRESS WITH LINKS!{RESET}")
        user_choice = input(f"      • {CYAN}2){RESET} {GREEN}SITE SCAN-STATUS_CODE{RESET}\n      • {CYAN}3){RESET} {YELLOW}About{RESET}\n\n      • {CYAN}0){RESET} {RED}Exit!{RESET} \n\n          {BLUE}PICK A NUMBER-->>{RESET} ").strip()
        
        if user_choice == "1":
            while True:
                os.system('clear')
                print(BANNER)
                user_ip = input(f"\n    • Enter Urls separated by ',' or 'B' to back! \n\n    {BLUE}-->{RESET} ").strip()
                if user_ip.lower() == 'b': break
                if user_ip == "": continue
                url_ip = [i.strip() for i in user_ip.split(",")]
                get_ip_address(url_ip)
                after = input(f"\n{BLUE}Scanning complete. Press Enter to back or 'C' to continue...{RESET}")
                if after.lower() != 'c': break
            
        elif user_choice == "2":
            while True:
                os.system('clear')
                print(BANNER)
                user_input = input(f"    • {BOLD}Enter URLs separated by commas (,) or 'B' to back! -->> {RESET}").strip()
                if user_input.lower() == 'b': break
                if user_input == "": continue
                url = [i.strip() for i in user_input.split(",")]
                SITE_BUSTER(url)
                input(f"\n{BLUE}Scanning complete. Press Enter to go back...{RESET}")
                break
        
        elif user_choice == "3":
            os.system('clear')
            print(BANNER)
            print(f"   {BLUE}> WHAT SITE-BUSTER EXACTLY DO!{RESET} \n   It provides server status codes.\n")
            input(f"\n{BLUE}Press Enter to go back...{RESET}")
            
        elif user_choice == "0":
            sys.exit()

if __name__ == "__main__":
    main_menu()
