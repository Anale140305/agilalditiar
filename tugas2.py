# Password yang benar
password_benar = "agil123"

# Memulai proses
while True:
    # Meminta input password dari pengguna
    password = input("Masukkan password Anda: ")

    # Mengecek apakah password benar
    if password == password_benar:
        print("Selamat datang bos!")
        break  # Keluar dari perulangan jika password benar
    else:
        print("Password salah, coba lagi!")  # Pesan kesalahan

# Pesan terima kasih setelah berhasil masuk
print("Terima kasih sudah menggunakan aplikasi kami.")