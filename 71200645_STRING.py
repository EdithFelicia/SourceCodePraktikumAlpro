# Universitas Kristen Duta Wacana
# Edith Felicia Putri

'''
Ani dan Andi ingin membuat permainan kata. Dengan ketentuan
sebagai berikut.
a. Pilihan katanya hanya: teman dan pulang yang lower. Selain
   itu user akan keluar dari program.
b. Kesempatan bermain hanya sekali.
c. Teman: Babak pertama dalam kalimat ada pilihan kata dan
   panjang kalimat lebih dari 10.
   Pulang: Babak pertama jumlah dari pilihan kata lebih dari 5.
d. Masing-masing pilihan kata hanya ada dua babak.
e. Babak kedua akan memanggil library random.
   Kata teman (Perkalian) dan kata pulang (perpangkatan).
'''

import random
nama = input("Masukkan nama: ")
pilihan_kata1 = 'teman'
pilihan_kata2 = 'pulang'
kata = input("Kata yang dipilih: ")
if kata in pilihan_kata1:
    print("-------------BABAK PERTAMA---------------")
    buat_kalimat = input("Kalimat: ")
    if pilihan_kata1 in buat_kalimat:
        panjang = (len(buat_kalimat))
        if panjang > 10:
            print("Mari lanjut bermain. Kamu pasti bisa!")
            print("---------------BABAK KEDUA---------------")
            print("Adu keberuntungan: Perkalian dua nilai dadu")
            nilai1 = random.randint(1, 6)
            nilai2 = random.randint(1, 6)
            print("Angka yang didapat ",nilai1, "dan", nilai2)
            hasil = nilai1 * nilai2
            if hasil > 10:
                ucapan = "selamat anda menang"
                print(ucapan.upper())
            else:
                print("Keberuntunganmu pasti ada di suatu tempat. Silakan mencoba lagi.")
        else:
            print("Anda kalah, silakan coba lagi lain kali.")
    else:
        print("Anda kalah, karena kata-kata tidak ada dalam kalimat.")

elif kata in pilihan_kata2:
    buat_kalimat = input("Kalimat: ")
    jumlah = (buat_kalimat.count(pilihan_kata2))
    if jumlah > 5:
        print("Mari lanjut bermain. Kamu pasti bisa!")
        print("--------------BABAK KEDUA--------------")
        print("Adu keberuntungan: Pembagian dua nilai dadu")
        nilai1 = random.randint(1, 6)
        nilai2 = random.randint(1, 6)
        print("Angka yang didapat ", nilai1, "dan", nilai2)
        hasil = nilai1 ** nilai2
        if hasil > 10:
            ucapan = "selamat anda menang"
            print(ucapan.upper())
        else:
            print("Keberuntunganmu pasti ada di suatu tempat. Silakan mencoba lagi.")
    else:
        print("Anda kalah, silakan coba lagi lain kali.")
else:
    print("Kata yang Anda masukkan tidak sesuai dengan pilihan kata yang ada.")


