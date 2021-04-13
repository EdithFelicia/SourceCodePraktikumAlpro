# Universitas Kristen Duta Wacana
# Edith Felicia Putri

'''
Tiana diminta oleh ibunya untuk memasukkan data belanja
yang harus dibelinya minggu nanti agar tidak mudah
hilang dalam file daftarbelanja.txt yang telah disediakan.
a. Ada kebutuhan rumah: pel, sapu, dkk.
b. Ada buah: Apel (5), Jeruk (4), dan Pisang (3).
c. Menampilkan list belanjaan di file.
d. Pilihan Exit.
'''

file = open('daftarbelanja.txt','w')
pembuka = file.write("Daftar Belanja TIANA\n")

while True:
    print("1.Kategori Kebutuhan Rumah")
    print("2.Kategori Buah")
    print("3.Tampilkan List Belanja")
    print("4.EXIT")
    user = int(input("Masukkan pilihan Anda: "))
    if user == 1:
        file.write("Kebutuhan Rumah: \n")
        kebutuhan = input("Isi kebutuhan: ")
        text = kebutuhan + "\n"
        file.write(text)
        continue
    if user == 2:
        file.write("Buah-buahan: \n")
        banyak_buah = int(input("Ada berapa buah yang mau dibeli: "))
        for i in range(banyak_buah):
            nama_buah = input("Buah: ")
            jumlah = input("Jumlah: ")
            buah = jumlah + " " + nama_buah + "\n"
            file.write(buah)
        continue
    if user == 3:
        file = open('daftarbelanja.txt','r')
        isi = file.read()
        print(isi)
        continue
    if user == 4:
        print("Selamat Berbelanja")
        break
    else:
        break

file.close()
