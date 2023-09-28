def hitung_nilai_akhir(uts, uas):
    # Fungsi ini akan menghitung nilai akhir berdasarkan nilai UTS dan UAS
    return 0.4 * uts + 0.6 * uas

def tampilkan_nilai_akhir(data_nilai_akhir):
    print("Hasil Nilai Akhir Mahasiswa:")
    for nama, nilai_akhir in data_nilai_akhir.items():
        print("Nama: {}\tNilai Akhir: {:.2f}".format(nama, nilai_akhir))

def main():
    data_mahasiswa = {
        # Data mahasiswa (nama sebagai key dan nilai UTS serta UAS sebagai value dalam bentuk tuple)
        "Asep": (100, 20),
        "Jamal": (50, 90),
        "Budi": (90, 95),
    }

    data_nilai_akhir = hitung_nilai_akhir_semua(data_mahasiswa)
    tampilkan_nilai_akhir(data_nilai_akhir)

    rata_rata_kelas = hitung_rata_rata(data_nilai_akhir)
    print("Rata-rata Kelas: {:.2f}".format(rata_rata_kelas))

    mahasiswa_tertinggi = mahasiswa_dengan_nilai_tertinggi(data_nilai_akhir)
    if mahasiswa_tertinggi:
        nama_tertinggi, nilai_tertinggi = mahasiswa_tertinggi
        print("Mahasiswa dengan Nilai Tertinggi:")
        print("Nama: {}\tNilai Akhir: {:.2f}".format(nama_tertinggi, nilai_tertinggi))
    else:
        print("Tidak ada data mahasiswa.")

if __name__ == "__main__":
    main()
