import requests
import os 

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
BOLD = "\033[1m"
RESET = "\033[0m"

BANNER = f"""
{RED}{BOLD} ____ ___ _____ _____  ___  _   _ ____ _____ 
/ ___|_ _|_   _| ____|  _ \\| | | / ___|_   _|
\\___ \\| |  | | |  _| | |_) | | | \\___ \\ | |  
 ___) | |  | | | |___|  _ <| |_| |___) || |  
|____/___| |_| |_____|_| \\_\\\\___/|____/ |_|  
{RESET}{YELLOW}     >> Advanced Multi-URL Recon Weapon <<
{RESET}"""

def SITE_BUSTER(url_list):
	print(f"             {BLUE}{BOLD}=== SITE-BUSTER ACTIVE ==={RESET}\n")
	for i in url_list:
		try:
			respons = requests.get(i, timeout=5)
			status = respons.status_code
			if status == 200:
				print(f"    {GREEN}[SUCCESS] {i} - Found! status: {status}{RESET}")
			elif status == 301 or status == 302:
				print(f"    {BLUE}[REDIRECT] {i} - Site moved to another location! status: {status}{RESET}")
			elif status == 400:
				print(f"    {YELLOW}[BAD REQUEST] {i} - Server could not understand request! status: {status}{RESET}")
			elif status == 401:
				print(f"    {RED}[UNAUTHORIZED] {i} - Login or credentials required! status: {status}{RESET}")
			elif status == 402:
				print(f"    {RED}[PAYMENT REQUIRED] {i} - Access locked behind a paywall! status: {status}{RESET}")
			elif status == 403:
				print(f"    {RED}{BOLD}[INTERESTING] {i} - This site is private/ no permission! status: {status}{RESET}")
			elif status == 404:
				print(f"    {YELLOW}[FAILED] {i} - You mistake or url not found! status: {status}{RESET}")
			elif status == 405:
				print(f"    {YELLOW}[METHOD NOT ALLOWED] {i} - Scanning method blocked by site! status: {status}{RESET}")
			elif status == 429:
				print(f"    {RED}[TOO MANY REQUESTS] {i} - Rate limit hit! Server blocking spam! status: {status}{RESET}")
			elif status == 500:
				print(f"    {RED}{BOLD}[SERVER ERROR] {i} - Server crashed internally! status: {status}{RESET}")
			elif status == 502:
				print(f"    {RED}[BAD GATEWAY] {i} - Main server communication broke down! status: {status}{RESET}")
			elif status == 503:
				print(f"    {RED}[OVERLOAD] {i} - Server down or traffic overload! status: {status}{RESET}")
			elif status == 504:
				print(f"    {RED}[TIMEOUT] {i} - Server took too long to respond! status: {status}{RESET}")
		except requests.exceptions.RequestException:
			print(f"    {RED}{BOLD}[ERROR] {i} - Connection failed!{RESET}")

def main_menu():
	while True:
		os.system('clear')
		print(BANNER)
		main_page = input(f"      • {GREEN}1) SITE SCAN-STATUS_CODE{RESET}\n      • {YELLOW}2) About{RESET}\n\n      • {RED}0) Exit!{RESET} \n\n          {BLUE}PICK A NUMBER-->>{RESET} ").strip()
		
		if main_page == "":
			continue
			
		elif main_page == "0":
			print(f"{RED} THANKS FOR USING THIS TOOL{RESET} ")
			print(f"{RED} THANKS FOR USING THIS TOOL .{RESET}")
			print(f"{RED} THANKS FOR USING THIS TOOL ..{RESET}")
			print(f"{RED} THANKS FOR USING THIS TOOL ...{RESET}")
			exit()
			
		elif main_page == "2":
			os.system('clear')
			print(BANNER)
			print(f"                              {YELLOW}{BOLD}ABOUT{RESET} \n                            —————————\n\n")
			print(f"   {BLUE}> HOW TO USE 'SITE-BUSTER' TOOL?{RESET}\n     ——————————————————————————————\n")
			print("   1) Go to main page and type '1' - SITE SCANNER—STATUS_CODE,,,\n   Now write a url or multiple \n   urls if you want!. For multiple urls when one url you writed \n   then for another use this ',' (comma) to write next url \n   Example -> \n   https://www.example.com,https://www.example.com... and more \n   you want!!\n")
			print(f"   {BLUE}> WHAT SITE-BUSTER EXACTLY DO!{RESET} \n     ————————————————————————————\n")
			print("   SITE-BUSTER, go and ask in the link to you provide if the \n   server reply then SITE-BUSTER say you status_code 200! which \n   is Success! if server doesn't reply or anything else then \n   SITE-BUSTER, provided you to the exact status_code which the \n   server provided. that means SITE-BUSTER only provided you server \n   status_code.\n")
			print(f"   {BLUE}> CREATOR/LINKS{RESET} \n     —————————————\n")
			print(f"   The creator name is 'TAMZID' \n")
			input(f"\n{BLUE}Press Enter to go back to Main Menu...{RESET}")
			
		elif main_page == "1":
			while True:
				os.system('clear')
				print(BANNER)
				user_input = input(f"    • {BOLD}Enter URLs separated by commas (,) or Type B to back! -->> {RESET}").strip()
				
				if user_input == "":
					continue
				elif user_input.lower() == "b":
					break
				else:
					os.system('clear')
					print(BANNER)
					url = [i.strip() for i in user_input.split(",")]
					SITE_BUSTER(url)
					input(f"\n{BLUE}Scanning complete. Press Enter to go back...{RESET}")
					break

if __name__ == "__main__":
	main_menu()
