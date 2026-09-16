# Pertemuan 03 Seleksi Python


**Nama:** Amandita Pebriana Putri  

**NIM:** 2225250134 

**Kelas:** 3A Pendidikan Matematika

---

## Tujuan
Praktikum ini bertujuan untuk memahami dan mengimplementasikan struktur seleksi kondisi pada bahasa pemrograman Python, meliputi penggunaan pernyataan `if`, `if-else`, kondisi majemuk dengan operator logika (`and`, `or`, `not`), serta `nested if` (if bersarang)[cite: 1].

---

## Cara Menjalankan

Buka Terminal di VS Code pada folder utama project, kemudian jalankan file yang ingin diuji dengan perintah berikut:

```bash
python latihan/01_genap_ganjil.py
python latihan/02_bandingkan_dua_bilangan.py
python latihan/03_kelulusan_bersyarat.py
python latihan/04_jenis_segitiga.py
python tugas/analisis_persamaan_kuadrat.py
```

---

## Algoritma Tugas

1. **Menerima Masukan:** Membaca input nilai koefisien $a$, $b$, dan $c$ dari pengguna sebagai bilangan desimal (*float*).
2. **Pemeriksaan Persamaan Kuadrat:** Memeriksa apakah nilai $a == 0$.
   - Jika $a == 0$, tampilkan pesan `"Bukan persamaan kuadrat."`
   - Jika $a \neq 0$, lanjutkan ke langkah perhitungan diskriminan.
3. **Perhitungan Diskriminan:** Menghitung nilai diskriminan dengan rumus $D = b^2 - 4ac$.
4. **Penentuan Jenis Akar:**
   - **Jika $D > 0$:** Hitung dua akar real berbeda menggunakan rumus $x_1 = \frac{-b + \sqrt{D}}{2a}$ dan $x_2 = \frac{-b - \sqrt{D}}{2a}$, lalu tampilkan keduanya.
   - **Jika $D == 0$:** Hitung satu akar real kembar menggunakan rumus $x = \frac{-b}{2a}$, lalu tampilkan nilainya.
   - **Jika $D < 0$:** Tampilkan pesan `"Tidak ada akar real."`
5. **Format Keluaran:** Menampilkan hasil perhitungan nilai diskriminan dan akar dengan format dua angka di belakang koma (`:.2f`).

---

## Hasil Pengujian

| Koefisien (a, b, c) | Nilai D | Hasil Diharapkan | Hasil Aktual | Status |
| :---: | :---: | :---: | :---: | :---: |
| `1, -5, 6` | `1.00` | Dua akar real: 3.00 dan 2.00 | Dua akar real: x1 = 3.00, x2 = 2.00 | Valid |
| `1, 2, 1` | `0.00` | Akar real kembar: -1.00 | Akar real kembar: x = -1.00 | Valid |
| `1, 0, 1` | `-4.00` | Tidak ada akar real | Tidak ada akar real | Valid |
| `0, 2, 3` | - | Bukan persamaan kuadrat | Bukan persamaan kuadrat | Valid |

---

## Refleksi

Dalam penyelesaian tugas praktikum Pertemuan 03 ini, kesalahan logika yang paling krusial terletak pada urutan eksekusi operator aritmetika saat menghitung akar real persamaan kuadrat. 

Jika penyebut $2a$ ditulis tanpa tanda kurung seperti `-b + d**0.5 / 2 * a`, Python akan melakukan pembagian terlebih dahulu baru dikalikan dengan $a$, sehingga menghasilkan nilai akar yang salah. Solusinya adalah mengelompokkan penyebut menggunakan tanda kurung wajib `(2 * a)`. Selain itu, memastikan kondisi pengecekan $a == 0$ berada di bagian paling awal sangat penting untuk mencegah terjadinya kesalahan *ZeroDivisionError*.

---

## Exit Ticket

1. Perbedaan Penting if dan if-else:
   - `if` tunggal hanya memiliki satu jalur aksi yang dieksekusi jika kondisi bernilai True (jika False, program langsung melewatinya).
   - `if-else` memiliki dua jalur aksi yang mutually exclusive—satu jalur dieksekusi jika True, dan jalur `else` wajib dieksekusi jika False.

2. Kesalahan Logika (Bug) dan Cara Memperbaikinya:
   - Kesalahan: Lupa memberikan tanda kurung pada penyebut `(2 * a)` saat menghitung akar kuadrat, serta lupa memeriksa kondisi `a == 0` di awal.
   - Perbaikan: Mengelompokkan penyebut menjadi `(2 * a)` agar pembagian dilakukan terhadap seluruh nilai penyebut, serta menambahkan struktur `if a == 0` di awal program untuk mencegah ZeroDivisionError.
