# Universitas Kristen Duta Wacana
# Edith Felicia Putri

'''
Raihan jarang sekali pergi ke gramedia, dan saat
mamanya mengajaknya, kali ini Raihan ingin membuat
daftar buku dalam bentuk list agar dia tidak lupa
buku apa saja yang ingin dia beli.

a. List tersebut langsung dapat membuat, menambah atau
   menghapus judul buku yang dia inginkan sesuai
   pilihannya. Kemudian list-nya diurutkan berdasarkan abjad.
   Data yang dihapus hanya bisa satu.
b. Jika memilih exit, maka keluar dari daftar.

'''

print("=====DAFTAR BUKU RAIHAN=====")
print("1. Membuat, Menambah, atau Mengurangi Judul Buku")
print("2. Exit")
user = int(input("Masukkan pilihan Anda: "))
if user == 1:
    buku = input("Judul buku yang diinginkan: ")
    buku = buku.split(", ")
    angka = 0
    for i in buku:
        angka = angka + 1
        print(angka,".",i)
    user_pilihan = input("Menambah atau Mengurang: ")
    if user_pilihan == 'Tambah':
        jumlah = int(input("Berapa banyak buku yang diinginkan: "))
        for i in range(jumlah):
            judul = input("Judul buku: ")
            buku.append(judul)
            angka = 0
            for j in buku:
                angka = angka + 1
                print(angka,".",j)
    elif user_pilihan == 'Kurang':
        judul_hapus = input("Judul buku: ")
        buku.remove(judul_hapus)

    buku.sort()
    print(" ")
    print("Bentuk List: ", buku)

elif user == 2:
    print("Anda telah keluar dari daftar.")

else:
    print(" ")

