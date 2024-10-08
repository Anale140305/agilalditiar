def hitung_gaji(nama, golongan, jam_kerja):
    if golongan == 'A':
        upah_per_jam = 5000
    elif golongan == 'B':
        upah_per_jam = 7000
    elif golongan == 'C':
        upah_per_jam = 8000
    elif golongan == 'D':
        upah_per_jam = 10000
    else:
        return "Golongan tidak valid!"
    
    if jam_kerja > 48:
        upah_lembur = (jam_kerja - 48) * 4000
    else:
        upah_lembur = 0
    
    gaji = (jam_kerja * upah_per_jam) + upah_lembur
    
    print(f"\nNama Karyawan: {nama}")
    print(f"Golongan: {golongan}")
    print(f"Jumlah jam kerja: {jam_kerja}")
    print(f"{nama} menerima upah Rp. {gaji} per minggu")
    return gaji

nama_karyawan = input("Masukkan nama karyawan: ")
golongan_karyawan = input("Masukkan golongan karyawan (A/B/C/D): ").upper()
jam_kerja_karyawan = int(input("Masukkan jumlah jam kerja: "))

hitung_gaji(nama_karyawan, golongan_karyawan, jam_kerja_karyawan)