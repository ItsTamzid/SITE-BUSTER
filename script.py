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
{RESET}{YELLOW}          >> Advanced Multi-URL Recon Weapon <<
{RESET}"""

def get_ip_address(domain_list):
    for domain in domain_list:
        try:
            clean_domain = domain.replace("http://", "").replace("https://", "").split('/')[0]
            ip_address = socket.gethostbyname(clean_domain)
            print(f"      {YELLOW}{domain}{RESET}  {BOLD}-->{RESET}  {GREEN}{ip_address}{RESET}")
        except socket.gaierror:
            print(f"      {YELLOW}{domain}{RESET}  {BOLD}-->{RESET}  {RED}Could not resolve domain.{RESET}")

def SITE_BUSTER(url_list):
    os.system('clear')
    print(BANNER)
    print(f"\n             {BLUE}{BOLD}=== GETING STATUS CODES ==={RESET}\n")
    
    for i in url_list:
        # यहाँ गणितीय रूप से चेक किया जा रहा है कि http या https मौजूद है या नहीं
        target_url = i
        if not target_url.startswith("http://") and not target_url.startswith("https://"):
            target_url = "https://" + target_url  # डिफ़ॉल्ट रूप से https जोड़ना

        try:
            respons = requests.get(target_url, timeout=5)
            status = respons.status_code
            if status == 200: print(f"    {GREEN}[SUCCESS] {target_url} - Found! status: {status}{RESET}")
            elif status in [301, 302]: print(f"    {BLUE}[REDIRECT] {target_url} - Site moved! status: {status}{RESET}")
            elif status == 404: print(f"    {YELLOW}[FAILED] {target_url} - Not found! status: {status}{RESET}")
            else: print(f"    {RED}[STATUS] {target_url} - Status code: {status}{RESET}")
        except requests.exceptions.RequestException:
            # यदि https से फ़ेल होता है और शुरुआत में यूजर ने http नहीं डाला था, तो http:// से प्रयास करें
            if i.startswith("http://") or i.startswith("https://"):
                print(f"    {RED}{BOLD}[ERROR] {target_url} - Connection failed!{RESET}")
            else:
                backup_url = "http://" + i
                try:
                    respons = requests.get(backup_url, timeout=5)
                    status = respons.status_code
                    if status == 200: print(f"    {GREEN}[SUCCESS] {backup_url} - Found! status: {status}{RESET}")
                    elif status in [301, 302]: print(f"    {BLUE}[REDIRECT] {backup_url} - Site moved! status: {status}{RESET}")
                    elif status == 404: print(f"    {YELLOW}[FAILED] {backup_url} - Not found! status: {status}{RESET}")
                    else: print(f"    {RED}[STATUS] {backup_url} - Status code: {status}{RESET}")
                except requests.exceptions.RequestException:
                    print(f"    {RED}{BOLD}[ERROR] {i} - Connection failed (Both HTTP/HTTPS)!{RESET}")

def main_menu():
    while True:
        time.sleep(0.6)
        os.system('clear')
        print(BANNER)
        print(f"      • {CYAN}1){RESET} {GREEN}GET IP-ADDRESS WITH LINKS!{RESET}")
        print(f"      • {CYAN}2){RESET} {GREEN}SITE SCAN-STATUS_CODE{RESET}")
        print(f"      • {CYAN}3){RESET} {YELLOW}About{RESET}\n")
        print(f"      • {CYAN}0){RESET} {RED}Exit!{RESET} \n")
        user_choice = input(f"          {BLUE}PICK A NUMBER-->>{RESET} ").strip()
        
        if user_choice == "1":
            time.sleep(0.5)
            while True:
                os.system('clear')
                print(BANNER)
                user_ip = input(f"\n    • Enter Urls separated by ',' or 'B' to back! \n\n    {BLUE}-->{RESET} ").strip()
                
                if user_ip.lower() == 'b':
                    time.sleep(0.7)
                    break
                    
                if user_ip == "":
                    time.sleep(0.7)
                    continue
                    
                url_ip = [i.strip() for i in user_ip.split(",")]
                get_ip_address(url_ip)
                after = input(f"\n\n{BLUE}Scanning complete. Press Enter to back or 'C' to continue...{RESET}")
                if after.lower() != 'c':
                    time.sleep(0.7)
                    break
            
        elif user_choice == "2":
            time.sleep(0.5)
            while True:
                os.system('clear')
                print(BANNER)
                user_input = input(f"    • {BOLD}Enter URLs separated by commas (,) or 'B' to back!{RESET}\n\n   {BLUE}-->> {RESET}").strip()
                if user_input.lower() == 'b':
                    time.sleep(0.7)
                    break
                if user_input == "":
                    time.sleep(0.7)
                    continue
                url = [i.strip() for i in user_input.split(",")]
                SITE_BUSTER(url)
                after_status_scan = input(f"\n{BLUE}Scanning complete. Press Enter to go back or Enter [b]...{RESET}")
                if after_status_scan == "":
                    time.sleep(0.7)
                    continue
                elif after_status_scan.lower() == "b":
                    time.sleep(0.7)
                    break
        
        elif user_choice == "3":
            time.sleep(0.7)
            os.system('clear')
            print(BANNER)
            print(f"                          {YELLOW}{BOLD}ABOUT{RESET} \n                         ———————\n\n")
            print(f"   {BLUE}> HOW TO USE 'SITE-BUSTER' TOOL?{RESET}\n     ——————————————————————————————\n")
            print("   1) Go to main page and type '1' - SITE SCANNER—STATUS_CODE,,,\n   Now write a url or multiple \n   urls if you want!. For multiple urls when one url you writed \n   then for another use this ',' (comma) to write next url \n   Example -> \n   https://www.example.com,https://www.example.com... and more \n   you want!!\n")
            print(f"   {BLUE}> WHAT SITE-BUSTER EXACTLY DO!{RESET} \n     ————————————————————————————\n")
            print("   SITE-BUSTER, go and ask in the link to you provide if the \n   server reply then SITE-BUSTER say you status_code 200! which \n   is Success! if server doesn't reply or anything else then \n   SITE-BUSTER, provided you to the exact status_code which the \n   server provided. that means SITE-BUSTER only provided you server \n   status_code.\n")
            input(f"\n{BLUE}Press Enter to go back to Main Menu...{RESET}")
            
        elif user_choice == "0":
            sys.exit()

if __name__ == "__main__":
    main_menu()
