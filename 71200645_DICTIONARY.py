# Universitas Kristen Duta Wacana
# Edith Felicia Putri

'''
Anita ingin mencatat kunci bangunan apartemen orang tuanya
menggunakan dictionary, agar ia tidak lupa, masing-masing
kunci cadangan dari tiap orang yang menyewa kamar di apartemen
tersebut. Dengan menulis nama penyewa, Anita bisa memperoleh
kunci juga informasi-informasi tentang penyewanya.
a. Ada lima orang yang menyewa apartemen kecilnya.
b. Kunci dikategorikan menjadi; A-Z. Jika salah memasukkan kunci
   maka proses penyimpanan diulang dari awal.

'''
penyewa = {}
draft = True
while draft:
    print("=====KUNCI APARTEMEN=====")
    print("1. Penyimpanan Kunci")
    print("2. Pencarian Kunci")
    print("3. Exit")
    pilihan = int(input("Masukkan pilihan Anda: "))
    if pilihan == 1:
        print("=====PENYIMPANAN KUNCI=====")
        simpan = True
        while simpan:
            nama = input("Nama Penyewa: ")
            kamar_sewa = input("Kamar yang disewa (A-Z): ")
            if kamar_sewa != kamar_sewa.upper() or int:
                print("Kunci tidak tersedia")
                break
            if kamar_sewa == kamar_sewa.upper():
                penyewa[nama] = kamar_sewa
                nama_lagi = input("Adakah kamar yang ingin disimpan lagi: ")
                if nama_lagi == 'yes':
                    simpan = True
                if nama_lagi == 'no':
                    simpan = False

    elif pilihan == 2:
        print("=====PENCARIAN KUNCI=====")
        nama_kunci = input("Masukkan nama: ")
        kunci = penyewa.get(nama_kunci,'tidak ada')
        print("Kunci dari " + nama_kunci + " adalah " + kunci)

    elif pilihan == 3:
        print("Anda telah keluar dari program")
        break

    else:
        print("Pilihan Anda tidak tersedia")
        break


