# SoccerMatch Tracker

*SoccerMatch Tracker* adalah aplikasi Python berbasis CLI (Command Line Interface) yang dibuat menggunakan konsep OOP (Object-Oriented Programming). Aplikasi ini membantu pengguna mencatat pertandingan sepak bola yang ditonton, termasuk skor, tim, tanggal pertandingan, serta informasi tambahan untuk pertandingan penting seperti kompetisi dan pemain terbaik.

Proyek ini terinspirasi dari hobi saya pribadi yang suka menonton sepak bola.

## Fitur Aplikasi

- Menambahkan pertandingan biasa dan pertandingan penting
- Menampilkan seluruh daftar pertandingan
- Mencari pertandingan berdasarkan nama tim
- Menyimpan dan membaca data secara otomatis menggunakan file JSON

## Struktur Folder
soccer_tracker/ ├── main.py ├── models/ │   ├── team.py │   ├── match.py │   └── manager.py ├── data/ │   └── matches.json (dibuat otomatis) ├── README.md

## Cara Menjalankan

1. Pastikan Python 3 sudah terinstal.
2. Buka terminal atau CMD, arahkan ke folder proyek.
3. Jalankan perintah:

```bash
python main.py 
```