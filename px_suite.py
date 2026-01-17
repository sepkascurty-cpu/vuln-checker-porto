import socket
import requests
from colorama import Fore, Style, init

# Inisialisasi warna
init(autoreset=True)

def show_banner():
    banner = f"""
    {Fore.CYAN}
    ██████╗ ██╗  ██╗      ███████╗██╗   ██╗██╗████████╗███████╗
    ██╔══██╗╚██╗██╔╝      ██╔════╝██║   ██║██║╚══██╔══╝██╔════╝
    ██████╔╝ ╚███╔╝ █████╗███████╗██║   ██║██║   ██║   █████╗  
    ██╔═══╝  ██╔██╗ ╚════╝╚════██║██║   ██║██║   ██║   ██╔════╝
    ██║     ██╔╝ ██╗      ███████║╚██████╔╝██║   ██║   ███████╗
    ╚═╝     ╚═╝  ╚═╝      ╚══════╝ ╚═════╝ ╚═╝   ╚═╝   ╚══════╝
    {Fore.GREEN}      >> Security Suite v1.6 | Anti-Zonk Mode | Created by: sepkascurty-cpu <<
    """
    print(banner)

def port_scanner():
    print(f"\n{Fore.YELLOW}[*] Starting Port Scanner...")
    target = input(f"{Fore.WHITE}Masukkan Target (IP/Domain): ").strip()
    common_ports = [21, 22, 23, 25, 53, 80, 110, 443, 3306, 8080]
    
    print(f"{Fore.CYAN}[+] Scanning {target}...\n")
    for port in common_ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"{Fore.GREEN}  [!] Port {port} is OPEN")
        s.close()
    print(f"\n{Fore.YELLOW}[*] Scan Selesai.")

def banner_grabber():
    print(f"\n{Fore.YELLOW}[*] Starting Banner Grabber...")
    target = input(f"{Fore.WHITE}Masukkan Target IP: ").strip()
    port = int(input(f"{Fore.WHITE}Masukkan Port: "))
    try:
        s = socket.socket()
        s.settimeout(3)
        s.connect((target, port))
        if port in [80, 443, 8080]:
            s.send(b"GET / HTTP/1.1\r\nHost: " + target.encode() + b"\r\n\r\n")
        
        banner = s.recv(1024).decode().strip()
        if banner:
            print(f"\n{Fore.GREEN}[SUCCESS] Banner: {Fore.WHITE}{banner}")
        else:
            print(f"{Fore.RED}[-] Port terbuka tapi tidak ada banner.")
        s.close()
    except Exception as e:
        print(f"{Fore.RED}[ERROR] Gagal: {e}")

def dir_buster():
    print(f"\n{Fore.YELLOW}[*] Starting Directory Buster...")
    target_url = input(f"{Fore.WHITE}Masukkan URL (tanpa http): ").strip()
    wordlist = ["admin", "login", "config", "backup", "v1", "api", "uploads", "phpmyadmin", "wp-admin", "secret"]
    
    print(f"{Fore.CYAN}[+] Mencari folder di http://{target_url}/ ...\n")
    for folder in wordlist:
        url = f"http://{target_url}/{folder}"
        try:
            response = requests.get(url, timeout=3, allow_redirects=False)
            if response.status_code == 200:
                print(f"{Fore.GREEN}  [200 OK]      -> {url}")
            elif response.status_code in [301, 302]:
                print(f"{Fore.CYAN}  [{response.status_code} REDIRECT] -> {url}")
            elif response.status_code == 403:
                print(f"{Fore.RED}  [403 FORBIDDEN]-> {url}")
            else:
                print(f"{Fore.WHITE}  [{response.status_code}] Mencoba: /{folder}")
        except:
            print(f"{Fore.RED}  [!] Error akses {folder}")
    print(f"\n{Fore.YELLOW}[*] Scan Selesai.")

def main():
    while True:
        show_banner()
        print(f"{Fore.WHITE}Menu Pilihan:")
        print(f"  1. Port Scanner")
        print(f"  2. Banner Grabber")
        print(f"  3. Directory Buster (Verbose Mode)")
        print(f"  4. Exit")
        
        choice = input(f"\n{Fore.GREEN}PX-Shell > ").strip()
        if choice == "1":
            port_scanner()
        elif choice == "2":
            banner_grabber()
        elif choice == "3":
            dir_buster()
        elif choice == "4":
            print(f"{Fore.RED}Mematikan sistem...")
            break
        else:
            print(f"{Fore.RED}[!] Pilihan salah!")
        input(f"\n{Fore.CYAN}Tekan Enter untuk kembali ke menu...")

if __name__ == "__main__":
    main()
