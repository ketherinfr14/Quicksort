def partisi(daftar, rendah, tinggi):
    """
    Fungsi untuk melakukan partisi pada daftar.
    Elemen yang lebih kecil dari pivot akan dipindahkan ke kiri,
    sedangkan yang lebih besar akan tetap di kanan.
    """
    pivot = daftar[tinggi]  # Memilih pivot
    i = rendah - 1  # Indeks untuk elemen yang lebih kecil
    
    for j in range(rendah, tinggi):
        if daftar[j] < pivot:
            i += 1
            daftar[i], daftar[j] = daftar[j], daftar[i]  # Tukar elemen
    
    daftar[i + 1], daftar[tinggi] = daftar[tinggi], daftar[i + 1]  # Tukar pivot ke posisi yang benar
    return i + 1

def pengurutan_cepat(daftar, rendah, tinggi):
    """
    Fungsi rekursif untuk mengurutkan daftar menggunakan algoritma QuickSort.
    """
    if rendah < tinggi:
        pi = partisi(daftar, rendah, tinggi)  # Mendapatkan indeks pivot setelah partisi
        pengurutan_cepat(daftar, rendah, pi - 1)  # Rekursi pada bagian kiri
        pengurutan_cepat(daftar, pi + 1, tinggi)  # Rekursi pada bagian kanan

def cetak_daftar(daftar):
    """
    Fungsi untuk mencetak daftar dalam format yang lebih mudah dibaca.
    """
    print("Daftar angka:", " ".join(map(str, daftar)))

# Program utama
def main():
    """
    Fungsi utama untuk menerima input dari pengguna dan menjalankan algoritma QuickSort.
    """
    try:
        daftar = list(map(int, input("Masukkan angka yang ingin diurutkan (pisahkan dengan spasi): ").split()))
        if not daftar:
            raise ValueError("Daftar angka tidak boleh kosong.")
        
        print("Daftar sebelum pengurutan:")
        cetak_daftar(daftar)
        
        pengurutan_cepat(daftar, 0, len(daftar) - 1)
        
        print("Daftar setelah pengurutan:")
        cetak_daftar(daftar)
    except ValueError:
        print("Harap masukkan angka yang valid!")

if __name__ == "__main__":
    main()
