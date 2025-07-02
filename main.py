from models.match import Match, ImportantMatch
from models.manager import MatchManager

def main():
    manager = MatchManager('data/matches.json')

    while True:
        print("\n=== Soccer Match Tracker ===")
        print("1. Tambah Pertandingan")
        print("2. Tampilkan Semua Pertandingan")
        print("3. Cari Pertandingan Berdasarkan Tim")
        print("4. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            tipe = input("Pertandingan penting? (y/n): ").lower()
            home = input("Tim Home: ")
            away = input("Tim Away: ")
            date = input("Tanggal (YYYY-MM-DD): ")
            score_home = int(input("Skor Home: "))
            score_away = int(input("Skor Away: "))

            if tipe == 'y':
                kompetisi = input("Kompetisi: ")
                best_player = input("Pemain Terbaik: ")
                match = ImportantMatch(home, away, date, score_home, score_away, kompetisi, best_player)
            else:
                match = Match(home, away, date, score_home, score_away)

            manager.add_match(match)
            print("Pertandingan berhasil ditambahkan!")

        elif pilihan == '2':
            matches = manager.view_matches()
            for m in matches:
                print(m)

        elif pilihan == '3':
            tim = input("Nama tim: ")
            hasil = manager.search_by_team(tim)
            if hasil:
                for m in hasil:
                    print(m)
            else:
                print("Tidak ditemukan pertandingan.")

        elif pilihan == '4':
            break

        else:
            print("Pilihan tidak valid.")

if __name__ == '__main__':
    main()
