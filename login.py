# ============================================
# LOGIN SYSTEM - Rule Based System
# ============================================
import os
import getpass
import time
import sys

# --- Konfigurasi Login ---
VALID_USERS = {
    "admin": "admin123",
    "kasir": "kasir123",
    "owner": "toko123"
}

# --- ANSI Colors ---
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def clear_screen():
    """Clear terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title="TOKO RULE BASED SYSTEM"):
    """Print header dengan border."""
    clear_screen()
    width = 50
    print(f"{Colors.CYAN}{'=' * width}{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}{title.center(width)}{Colors.ENDC}")
    print(f"{Colors.CYAN}{'=' * width}{Colors.ENDC}")
    print()

def print_box(content_lines, color=Colors.BLUE):
    """Print content dalam box."""
    width = 40
    print(f"{color}{'─' * width}{Colors.ENDC}")
    for line in content_lines:
        print(f"{color}│ {line:<37}│{Colors.ENDC}")
    print(f"{color}{'─' * width}{Colors.ENDC}")

def animate_loading(text="Loading", duration=1.5):
    """Animasi loading sederhana."""
    for i in range(3):
        sys.stdout.write(f"\r{text}{'.' * (i + 1)}{' ' * (2 - i)}")
        sys.stdout.flush()
        time.sleep(duration / 3)
    print()

def login_page():
    """Halaman login utama."""
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        print_header("TOKO RULE BASED SYSTEM")

        print(f"{Colors.BOLD}{Colors.CYAN}          SELAMAT DATANG{Colors.ENDC}")
        print(f"{Colors.CYAN}     Rule Based System + Forward Chaining{Colors.ENDC}")
        print()

        # Box login
        print_box([
            f"{Colors.BOLD}LOGIN AKUN ANDA{Colors.ENDC}",
            "",
            "Username: ",
            "Password: "
        ])

        # Input
        try:
            username = input(f"\n{Colors.GREEN}➤ Username: {Colors.ENDC}").strip()
            password = getpass.getpass(f"{Colors.GREEN}➤ Password: {Colors.ENDC}")
        except (KeyboardInterrupt, EOFError):
            print(f"\n{Colors.FAIL}Login dibatalkan.{Colors.ENDC}")
            return None

        # Validasi
        if not username or not password:
            print(f"\n{Colors.WARNING}⚠ Username dan password harus diisi!{Colors.ENDC}")
            time.sleep(1.5)
            continue

        if username in VALID_USERS and VALID_USERS[username] == password:
            print(f"\n{Colors.GREEN}✓ Login berhasil! Selamat datang, {username}!{Colors.ENDC}")
            animate_loading("Membuka sistem")
            return username
        else:
            attempts += 1
            remaining = max_attempts - attempts
            print(f"\n{Colors.FAIL}✗ Username atau password salah!{Colors.ENDC}")
            if remaining > 0:
                print(f"{Colors.WARNING}  Sisa percobaan: {remaining}{Colors.ENDC}")
                time.sleep(1.5)
            else:
                print(f"\n{Colors.FAIL}{Colors.BOLD}⚠ Akun dikunci. Hubungi administrator.{Colors.ENDC}")
                time.sleep(2)
                return None

    return None

def show_user_info(username):
    """Tampilkan info user setelah login."""
    print()
    print_box([
        f"{Colors.GREEN}{Colors.BOLD}LOGIN BERHASIL{Colors.ENDC}",
        "",
        f"Username: {Colors.BOLD}{username}{Colors.ENDC}",
        f"Role: {Colors.CYAN}{'Admin' if username == 'admin' else 'Kasir'}{Colors.ENDC}",
        f"Waktu: {time.strftime('%H:%M:%S')}"
    ], color=Colors.GREEN)

def main():
    """Main entry point."""
    clear_screen()

    # Cek apakah getpass tersedia di Termux
    try:
        import termios
    except ImportError:
        # Fallback untuk Termux/Android
        import subprocess
        def getpass_fallback(prompt=""):
            print(prompt, end="", flush=True)
            result = subprocess.run(["stty", "-echo"], capture_output=True)
            try:
                password = input()
            finally:
                subprocess.run(["stty", "echo"], capture_output=True)
            print()
            return password

    # Login
    username = login_page()

    if username is None:
        print_header("TOKO RULE BASED SYSTEM")
        print(f"{Colors.FAIL}{Colors.BOLD}  GAGAL LOGIN{Colors.ENDC}")
        print(f"{Colors.FAIL}  Silahkan hubungi administrator.{Colors.ENDC}")
        print()
        return

    # Tampilkan info user
    show_user_info(username)
    time.sleep(2)

    # Menu utama akan dihandle di file terpisah
    print(f"\n{Colors.CYAN}Membuka menu utama...{Colors.ENDC}")
    animate_loading("Loading")

    # Import dan jalankan menu utama
    try:
        import menu_utama
        menu_utama.main(username)
    except ImportError:
        print(f"{Colors.WARNING}Menu utama tidak ditemukan. Jalankan menu_utama.py{Colors.ENDC}")
        # Fallback: langsung jalankan demo
        try:
            import toko
        except ImportError:
            print(f"{Colors.FAIL}toko.py tidak ditemukan.{Colors.ENDC}")

if __name__ == "__main__":
    main()
