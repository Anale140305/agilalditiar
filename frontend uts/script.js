function hitungBiaya() {
    const beratBarang = parseFloat(document.getElementById('beratBarang').value);
    const kotaAsal = document.getElementById('kotaAsal').value;
    const kotaTujuan = document.getElementById('kotaTujuan').value;

    if (!beratBarang || !kotaAsal || !kotaTujuan) {
        alert('Mohon lengkapi semua data!');
        return;
    }

    let biayaBerat = 0;
    if (beratBarang <= 1) {
        biayaBerat = 1500;
    } else if (beratBarang <= 5) {
        biayaBerat = 2500;
    } else if (beratBarang <= 10) {
        biayaBerat = 3500;
    } else {
        biayaBerat = 4500;
    }

    const biayaJarak = {
        "banyuwangi": { "banyuwangi": 5000, "jember": 7500, "probolinggo": 10000, "surabaya": 15000 },
        "jember": { "banyuwangi": 7500, "jember": 5000, "probolinggo": 8500, "surabaya": 12500 },
        "probolinggo": { "banyuwangi": 10000, "jember": 8500, "probolinggo": 5000, "surabaya": 6500 },
        "surabaya": { "banyuwangi": 15000, "jember": 12500, "probolinggo": 6500, "surabaya": 5000 }
    };

    const biayaJarakTotal = biayaJarak[kotaAsal][kotaTujuan];
    const totalBiaya = biayaBerat + biayaJarakTotal;

    document.getElementById('totalBiaya').value = totalBiaya;
}