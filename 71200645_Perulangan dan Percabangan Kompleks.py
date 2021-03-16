# Edith Felicia Putri
# Universitas Kristen Duta Wacana

'''
Guru Matematika Andrew ingin membuat program absensi murid
di akhir tahun ajaran yang harus diisi oleh murid kelasnya
sendiri.
a. Hal-hal yang ditampilkan: Alfa, sakit, izin, dan selesai.
   Selain ini, murid langsung keluar dari program.
b. apabila alfanya sudah lebih dari tiga kali, maka program
   akan menampilkan permohonan maaf sebanyak 12 baris dari
   murid tersebut.
c. Apabila murid memiliki surat dari dokter, maka ia bebas, sementara
   bagi yang tidak ada diberi peringatan.
d. Murid juga bisa keluar dari program apabila sudah mengisi
   seluruh absen.
e. Jawaban dari pertanyaan yang diberikan haruslah iya dan tidak.
'''

print("PROGRAM ABSEN KELAS")
nama = input("Nama Murid: ")
absensi = 3
while absensi < 4:
    print("KETERANGAN")
    print("1. Alfa")
    print("2. Sakit")
    print("3. Izin")
    print("4. Selesai")
    pilihan = int(input("Silakan isi data absen satu persatu: "))
    if pilihan == 1:
        absen = int(input("Sudah berapa kali kamu absen alfa: "))
        if absen > 3:
            for i in range(1, 12):
                print("Saya, ", nama, " berjanji tidak akan absen alfa tanpa alasan yang jelas lagi")
        elif absen >= 0:
            print("Tetap jadi anak yang rajin, dan lanjutkan sampai kelulusan")
    elif pilihan == 2:
        sakit = int(input("Sudah berapa kali kamu absen sakit (1 - 3): "))
        if sakit == 0:
            continue
        elif sakit < 4:
            tanya = input("Adakah surat keterangan dari dokter: ")
            if tanya == 'iya':
                print("Surat akan dicek lagi oleh guru")
                print("Kamu sudah absen sakit sebanyak", sakit)
            elif tanya == 'tidak':
                print("Lain kali harus ada surat keterangan")
        elif sakit > 4:
            print("Kamu harus konsultasi sama guru")
    elif pilihan == 3:
        alasan = input("Ada kegiatan apa (Akademik maupun Nonakademik): ")
        print("Terus banggakan nama sekolah!")
    elif pilihan == 4:
        tanya1 = input("Sudahkah kamu mengisi semua absen di atas: ")
        if tanya1 == 'iya':
            break
        elif tanya1 == 'tidak':
            continue
    else:
        absensi = 5
        if absensi > 4:
            print("Pilihan kamu tidak tersedia di program ini.")
            break