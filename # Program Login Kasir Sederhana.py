# Program Login Kasir Sederhana
# Simpan file ini dengan nama: login_kasir.py

# Data kasir (username dan password)
data_kasir = {
    'kasir1': {'password': '123', 'nama': 'Budi Santoso'},
    'kasir2': {'password': '456', 'nama': 'Siti Aminah'},
    'admin': {'password': 'admin', 'nama': 'Administrator'}
}

def clear_screen():
    """Fungsi untuk membersihkan layar"""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_header():
    """Fungsi untuk menampilkan header"""
    print("=" * 50)
    print("          SISTEM LOGIN KASIR")
    print("=" * 50)
    print()

def login():
    """Fungsi untuk melakukan login"""
    tampilkan_header()
    
    print("Silakan login terlebih dahulu\n")
    
    # Input username dan password
    username = input("Username: ")
    password = input("Password: ")
    
    # Cek username dan password
    if username in data_kasir:
        if data_kasir[username]['password'] == password:
            # Login berhasil
            return True, username
        else:
            # Password salah
            print("\n❌ Password salah!")
            return False, None
    else:
        # Username tidak ditemukan
        print("\n❌ Username tidak ditemukan!")
        return False, None

def dashboard(username):
    """Fungsi untuk menampilkan dashboard setelah login"""
    clear_screen()
    nama = data_kasir[username]['nama']
    
    print("=" * 50)
    print("            DASHBOARD KASIR")
    print("=" * 50)
    print(f"\n✅ Login Berhasil!")
    print(f"\nSelamat datang, {nama}!")
    print(f"Username: {username}")
    print("\n" + "=" * 50)
    print("\nAnda sudah berhasil masuk ke sistem kasir.")
    print("=" * 50)

def main():
    """Fungsi utama program"""
    while True:
        clear_screen()
        
        # Proses login
        berhasil, username = login()
        
        if berhasil:
            # Jika login berhasil, tampilkan dashboard
            input("\nTekan Enter untuk melanjutkan...")
            dashboard(username)
            
            # Menu logout
            print("\n")
            pilihan = input("Ketik 'logout' untuk keluar atau Enter untuk tetap di dashboard: ")
            if pilihan.lower() == 'logout':
                print("\n✅ Logout berhasil. Terima kasih!")
                break
        else:
            # Jika login gagal, tanya apakah ingin coba lagi
            print()
            coba_lagi = input("Coba login lagi? (y/n): ")
            if coba_lagi.lower() != 'y':
                print("\nTerima kasih!")
                break

# Jalankan program
if __name__ == "__main__":
    print("\n📝 INFO AKUN DEMO:")
    print("-" * 50)
    print("Username: kasir1 | Password: 123")
    print("Username: kasir2 | Password: 456")
    print("Username: admin  | Password: admin")
    print("-" * 50)
    input("\nTekan Enter untuk memulai...")
    
    main()