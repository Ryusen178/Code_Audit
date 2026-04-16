# 🧾 Code Audit - Aplikasi Kasir Sederhana (Python CLI)

## 📌 Deskripsi Project

Project ini dibuat untuk memenuhi tugas **Code Audit (Clean Code)**.
Aplikasi yang digunakan sebagai studi kasus adalah **Aplikasi Kasir Sederhana berbasis Command Line Interface (CLI) menggunakan Python**.

Tujuan utama project ini adalah:

* Mengidentifikasi pelanggaran prinsip Clean Code
* Melakukan refactor (perbaikan kode)
* Membandingkan kode sebelum dan sesudah perbaikan

---

## 📂 Struktur Project

```
code-audit-kasir/
│
├── kasir_trash.py   # Kode awal (belum clean code)
├── kasir_clean.py   # Kode hasil perbaikan (clean code)
└── README.md
```

---

## 🚀 Cara Menjalankan Program

1. Pastikan Python sudah terinstall
2. Buka terminal di folder project
3. Jalankan perintah:

```bash
python kasir_clean.py
```

4. Masukkan data barang sesuai instruksi di terminal

---

## 🔍 Code Audit (Temuan Masalah)

Berikut beberapa pelanggaran Clean Code pada kode awal:

1. ❌ **Poor Naming**

   * Nama fungsi tidak deskriptif (`h`, `d`, `x`)

2. ❌ **Melanggar Single Responsibility Principle (SRP)**

   * Satu fungsi menangani banyak tugas sekaligus

3. ❌ **Magic Number**

   * Nilai langsung ditulis di kode (`100000`, `0.1`)

4. ❌ **Tidak Ada Validasi Input**

   * Program bisa error jika input tidak sesuai

5. ❌ **Struktur Program Tidak Rapi**

   * Tidak ada pemisahan fungsi yang jelas

---

## ✅ Perbaikan (Implementasi Clean Code)

Perbaikan yang dilakukan pada kode:

* ✔️ Menggunakan **nama fungsi yang jelas dan deskriptif**
* ✔️ Menerapkan **Single Responsibility Principle (SRP)**
* ✔️ Mengganti magic number dengan **konstanta**
* ✔️ Menambahkan **error handling (try-except)**
* ✔️ Menggunakan struktur program yang lebih rapi (`main()`)

---

## 📊 Perbandingan Sebelum & Sesudah

| Aspek       | Sebelum                 | Sesudah                        |
| ----------- | ----------------------- | ------------------------------ |
| Naming      | Tidak jelas             | Deskriptif & mudah dipahami    |
| Struktur    | Semua dalam satu fungsi | Dipisah berdasarkan fungsi     |
| Validasi    | Tidak ada               | Ada validasi input             |
| Konstanta   | Hardcoded               | Menggunakan variabel konstanta |
| Readability | Sulit dibaca            | Lebih rapi & jelas             |

---

## 🎯 Kesimpulan

Setelah dilakukan refactor, kode menjadi lebih:

* Mudah dibaca (readable)
* Mudah dipelihara (maintainable)
* Lebih terstruktur
* Sesuai dengan prinsip Clean Code

---

## 👤 Author

Nama: **(Saifullah Yusuf)**
NIM: **(2411102441083)**
Kelas: **(Rekayasa Pernagkat Lunak)**

---
