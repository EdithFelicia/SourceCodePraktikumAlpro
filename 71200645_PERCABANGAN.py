# Universitas Kristen Duta Wacana
# Edith Felicia Putri

'''

Siska menginginkan sebuah program untuk mempermudahnya menjual foto
berkarakter Little Nightmares. Setiap foto memiliki pesannya sendiri
disertai nama pelanggan dan diakhir memberitahu pada pelanggan harga
dari foto tersebut berdasarkan jumlah yang ingin mereka beli.
Berikut ini ketentuan lebih jauh dari program yang diinginkan Siska.

a. Di latar belakang Pale City, Mono bisa memilih ingin berfoto dengan
   Thin Man atau Viewers, sementara Bullies atau Teacher tersedia di latar belakang School.
b. Harga sebuah foto dengan latar belakang dan karakter apa pun adalah Rp50.000
c. Jika Mono berfoto dengan Bullies dan Thin Man, pelanggan mendapat diskon random

'''

import random
print("----------LITTLE NIGHTMARES PHOTOSHOOT----------")
print("Karakter Anda adalah Mono")
nama = input("Nama Anda : ")
print("Silakan pilih latar belakang: ")
print("1. Pale City")
print("2. School")
pilihan = int(input("Masukkan pilihan Anda: "))
harga = 50000

if pilihan == 1:
    print("Tidak ada tempat yang melambangkan kesunyian melebihi Pale City")
    print("Dengan siapa kamu ingin di sini?")
    print("1. Thin Man")
    print("2. Viewers")
    user = int(input("Silakan pilih temanmu: "))
    if user == 1:
        angka = random.randint(10, 50)
        print("Selamat bercengkrama,",nama,"!")
        print("Pertemuan yang sangat indah ini menghadirkan diskon sebesar",angka,"%")
        diskon = angka / 100 * harga
        besar_diskon = harga - diskon
        print("Dia sudah menanti kedatanganmu sejak lama dengan memberikan foto ini seharga Rp",besar_diskon)
        buah_foto = int(input("Berapa buah foto yang kamu inginkan :"))
        print("Anda membayar foto ini sebesar", besar_diskon * buah_foto)
    else:
        print("Bukankah nasib mereka mengerikan,",nama,"?")
        print("Televisi benar-benar mengubah hidup seseorang ya!")
        buah_foto = int(input("Berapa buah foto yang Anda inginkan: "))
        print("Anda membayar foto ini sebesar Rp", buah_foto * harga)
else:
    print("Dimana kamu menuntun ilmu selama ini, kalau bukan sekolah?")
    print("Dengan siapa kamu ingin di sini?")
    print("1. Bullies")
    print("2. Teacher")
    user = int(input("Silakan pilih temanmu: "))
    if user == 1:
        angka = random.randint(10, 50)
        print("Selamat bersenang-senang,",nama,"!")
        print("Salah seorang Bully menyerakkan koin saat kau menghancurkan kepalanya")
        print("Foto ini mendapat diskon sebesar", angka, '%')
        diskon = (angka / 100) * harga
        besar_diskon = harga - diskon
        print("Harga foto ini menjadi Rp", besar_diskon)
        buah_foto = int(input("Berapa buah foto yang Anda inginkan: "))
        print("Anda membayar foto ini sebesar Rp", besar_diskon * buah_foto)
    else:
        print("Selamat bersembunyi,",nama,"!")
        print("Tetap rajin belajar dan mengerjakan tugas dengan baik ya!")
        buah_foto = int(input("Berapa buah foto yang Anda inginkan: "))
        print("Anda membayar foto ini sebesar Rp", harga * buah_foto)

print("Terima kasih sudah hadir!")
