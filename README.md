# **Simulasi Gerak Jatuh Bebas Menggunakan Metode Numerik Euler**

## Ibnu Zaky Fauzi - 2306161870

## Deskripsi Program

Program ini dibuat untuk mensimulasikan gerak jatuh bebas suatu benda di bawah pengaruh gaya gravitasi menggunakan metode numerik **Euler**. Model matematika didasarkan pada hukum Newton II, di mana benda dijatuhkan dari ketinggian tanpa kecepatan awal.

Program ini diimplementasikan dalam bahasa pemrograman **C**, dengan membagi waktu jatuh menjadi sejumlah interval diskrit (dengan langkah waktu tertentu), kemudian menghitung perubahan posisi dan kecepatan secara iteratif.

Metode Euler digunakan untuk mengaproksimasi nilai dari persamaan diferensial secara numerik, yang menghasilkan estimasi waktu jatuh dan kecepatan akhir saat benda menyentuh tanah.

### Fitur utama program:
- Mendefinisikan parameter fisika: posisi awal, kecepatan awal, percepatan gravitasi.
- Membagi waktu menjadi titik-titik diskrit.
- Menggunakan metode Euler untuk menghitung posisi dan kecepatan setiap langkah waktu.
- Menampilkan tabel hasil iterasi: waktu, posisi, dan kecepatan.
- Menghentikan simulasi secara otomatis ketika posisi ≤ 0 (benda menyentuh tanah).

---

## Deskripsi Program Python untuk Grafik

Visualisasi data hasil simulasi dilakukan menggunakan program Python dengan library **Matplotlib**. Grafik yang ditampilkan meliputi:

- **Grafik posisi terhadap waktu (x vs t)**  
  Menunjukkan penurunan posisi benda secara non-linear seiring waktu.
- **Grafik kecepatan terhadap waktu (v vs t)**  
  Menunjukkan peningkatan linear kecepatan akibat percepatan gravitasi konstan.

### Fungsi kode Python:
- Membaca hasil simulasi dari program C.
- Membuat array waktu, posisi, dan kecepatan.
- Menampilkan dua grafik terpisah:
  1. Posisi terhadap waktu
  2. Kecepatan terhadap waktu

Visualisasi ini membantu memverifikasi hasil perhitungan numerik dan memberikan pemahaman visual terhadap dinamika sistem gerak jatuh bebas.

---

## Catatan:
Kode sumber **C** dan **Python**, serta grafik hasil simulasi dapat ditemukan dalam folder repository ini.
