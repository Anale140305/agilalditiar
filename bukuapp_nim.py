from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Membuat koneksi ke database
def init_db():
    conn = sqlite3.connect('perpus_nim.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS buku_nim (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Kode_Buku TEXT NOT NULL,
            Nama_Buku TEXT NOT NULL,
            Penerbit TEXT,
            Pengarang TEXT,
            Jumlah_Buku INTEGER
        )
    ''')
    conn.commit()
    conn.close()

# Route untuk halaman utama
@app.route('/')
def index():
    conn = sqlite3.connect('perpus_nim.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM buku_nim')
    buku = cursor.fetchall()
    conn.close()
    return render_template('index_nim.html', buku=buku)

# Route untuk menambah data buku
@app.route('/tambah', methods=['GET', 'POST'])
def tambah():
    if request.method == 'POST':
        # Debugging: tampilkan semua data form
        print(request.form)  # Akan menampilkan semua field yang dikirim
        kode_buku = request.form.get('Kode_Buku', '')
        nama_buku = request.form.get('Nama_Buku', '')
        penerbit = request.form.get('Penerbit', '')
        pengarang = request.form.get('Pengarang', '')
        jumlah_buku = request.form.get('Jumlah_Buku', '')

        print(f"Kode Buku: {kode_buku}, Nama Buku: {nama_buku}, Jumlah Buku: {jumlah_buku}")  # Debugging

        if not kode_buku or not nama_buku or not jumlah_buku:
            return "Semua field harus diisi", 400

        conn = sqlite3.connect('perpus_nim.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO buku_nim (Kode_Buku, Nama_Buku, Penerbit, Pengarang, Jumlah_Buku)
            VALUES (?, ?, ?, ?, ?)
        ''', (kode_buku, nama_buku, penerbit, pengarang, jumlah_buku))

        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    
    return render_template('tambah_nim.html')

# Route untuk mengedit data buku
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    conn = sqlite3.connect('perpus_nim.db')
    cursor = conn.cursor()

    if request.method == 'POST':
        kode_buku = request.form.get('Kode_Buku', '')
        nama_buku = request.form.get('Nama_Buku', '')
        penerbit = request.form.get('Penerbit', '')
        pengarang = request.form.get('Pengarang', '')
        jumlah_buku = request.form.get('Jumlah_Buku', '')

        if jumlah_buku:
            try:
                jumlah_buku = int(jumlah_buku)
            except ValueError:
                return "Jumlah Buku harus berupa angka", 400
        else:
            jumlah_buku = 0  # Set nilai default jika kosong

        cursor.execute('''
            UPDATE buku_nim
            SET Kode_Buku = ?, Nama_Buku = ?, Penerbit = ?, Pengarang = ?, Jumlah_Buku = ?
            WHERE id = ?
        ''', (kode_buku, nama_buku, penerbit, pengarang, jumlah_buku, id))

        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    cursor.execute('SELECT * FROM buku_nim WHERE id = ?', (id,))
    buku = cursor.fetchone()
    conn.close()
    return render_template('edit_nim.html', buku=buku)

# Inisialisasi database saat aplikasi dijalankan
if __name__ == '__main__':
    init_db()
    app.run(debug=True)