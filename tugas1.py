# Meminta input total belanja dari pengguna
total_belanja = float(input("Masukkan total belanja Anda: "))

# Mengecek apakah total belanja >= 100.000
if total_belanja >= 100.000:
    print("Selamat! Anda dapat hadiah.")

else:
    print("Terima kasih sudah belanja.")