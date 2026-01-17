import socket

def grab_banner(ip, port):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((ip, port))
        # Mengambil data banner dari server
        banner = s.recv(1024).decode().strip()
        return banner
    except:
        return None

def check_vulnerabilities(banner):
    # Daftar software jadul yang biasanya punya celah (contoh)
    vulnerable_banners = [
        "SSH-1.99-OpenSSH_2.3",
        "Apache/2.2.15",
        "vsFTPd 2.3.4"
    ]
    for vuln in vulnerable_banners:
        if vuln in banner:
            return f"[!] BAHAYA: Versi {vuln} terdeteksi! (Potensi Celah Keamanan)"
    return "[+] Versi aman atau tidak dikenal."

target_ip = input("Masukkan IP Target (misal 192.168.94.1): ")
port_list = [21, 22, 80] # Port umum: FTP, SSH, HTTP

for port in port_list:
    print(f"Checking Port {port}...")
    banner = grab_banner(target_ip, port)
    if banner:
        print(f"   [Banner]: {banner}")
        print(f"   [Status]: {check_vulnerabilities(banner)}")
    else:
        print(f"   [Status]: Tidak ada respon.")
