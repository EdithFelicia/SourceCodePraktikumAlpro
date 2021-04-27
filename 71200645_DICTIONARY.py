# Universitas Kristen Duta Wacana
# Edith Felicia Putri

'''
Anita ingin mencatat kunci bangunan apartemen orang tuanya
menggunakan dictionary, agar ia tidak lupa, masing-masing
kunci cadangan dari tiap orang yang menyewa kamar di apartemen
tersebut. Dengan menulis nama penyewa, Anita bisa memperoleh
kunci.
a. Ada lima orang yang menyewa apartemen kecilnya.
b. Kunci dikategorikan menjadi; A-Z.
'''

penyewa = {}
daftar = True
while daftar:
    print("=====KUNCI APARTEMEN=====")
    print("1. Penyimpanan Kunci")
    print("2. Pencarian Kunci")
    print("3. Exit")
    pilihan = int(input("Masukkan pilihan Anda: "))
    if pilihan == 1:
        print("=====PENYIMPANAN KUNCI=====")
        simpan = True
        while simpan:
            nama = input("Masukkan nama: ")
            kamar_sewa = input("Kunci kamar yang disewa (A-Z): ")
            if kamar_sewa == kamar_sewa.upper():
                penyewa[nama] = kamar_sewa
                nama_lagi = input("Ada nama penyewa lagi yang ingin disimpan: ")
                if nama_lagi == 'yes':
                    simpan = True
                if nama_lagi == 'no':
                    simpan = False
                    print(penyewa)
                    break
            else:
                break
    elif pilihan == 2:
        print("=====PENCARIAN KUNCI=====")
        nama_kunci = input("Masukkan nama penyewa: ")
        kunci = penyewa.get(nama_kunci,'tidak ada')
        print("Kunci dari " + nama_kunci + " adalah " + kunci)

    elif pilihan == 3:
        print("Anda telah keluar dari program")
        break

    else:
        print("Pilihan Anda tidak tersedia")
        break