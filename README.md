# 📚 **Laporan Tugas: Implementasi Client-Server dan Kriptografi DES**

![Status](https://img.shields.io/badge/Status-Tugas_Selesai-brightgreen?style=flat-square)
![Tipe](https://img.shields.io/badge/Tipe-Tugas_Keamanan_Informasi-blue?style=flat-square)

## Deskripsi Proyek

Proyek ini merupakan tugas kelompok yang mengimplementasikan komunikasi **client-server** dengan penerapan algoritma **DES (Data Encryption Standard)**. Tugas ini bertujuan untuk memahami dan mempraktikkan komunikasi antar perangkat dengan kriptografi dasar.

---

## 👥 **Anggota Kelompok**

| Nama                                | NRP        |
| ----------------------------------- | ---------- |
| **GLORIYANO CRISTHO DANIEL PEPUHO** | 5025201121 |
| **RIYANDA CAVIN SINAMBELA**         | 5025221100 |

---

## 🗂 **Pembagian Tugas**

### 1. Modul `client.py`

- **Tanggung Jawab:**

  - Implementasi antarmuka client dan fungsi terkait komunikasi dengan server.
  - Penanganan input dan output user.

  **Dikerjakan oleh:** Riyanda Cavin Sinambela

---

### 2. Modul `des.py`

- **Tanggung Jawab:**

  - Implementasi algoritma kriptografi DES.
  - Dokumentasi logika enkripsi dan dekripsi.

  **Dikerjakan oleh:** GLORIYANO CRISTHO DANIEL PEPUHO

---

---

### 3. Modul `library.py`

- **Tanggung Jawab:**

  - Menyediakan fungsi dan utilitas umum yang digunakan oleh modul lain.
  - Optimasi kode dan pemisahan fungsi reusable.

  **Dikerjakan oleh:** GLORIYANO CRISTHO DANIEL PEPUHO

---

---

### 4. Modul `logic.py`

- **Tanggung Jawab:**

  - Mengembangkan logika utama yang menghubungkan semua modul.
  - Integrasi fungsi dari library ke dalam alur sistem.

  **Dikerjakan oleh:** Riyanda Cavin Sinambela

---

### 5. Modul `server.py`

- **Tanggung Jawab:**

  - Menyusun server dan mekanisme komunikasi dengan client.
  - Memastikan koneksi berjalan dengan baik dan menangani request-response.

  **Dikerjakan oleh:** GLORIYANO CRISTHO DANIEL PEPUHO

---

## Cara Menjalankan Proyek

1. Clone repository ini:

   ```bash
   git clone https://github.com/rcsinambela/des-client-server.git
   ```

2. Masuk ke direktori proyek:

   ```bash
   cd des-client-server
   ```

3. Jalankan server:

   ```bash
   python server.py
   ```

4. Jalankan client di terminal lain:

   ```bash
   python client.py
   ```
