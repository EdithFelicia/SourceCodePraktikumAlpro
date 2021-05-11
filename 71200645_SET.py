# Universitas Kristen Duta Wacana
# Edith Felicia Putri

'''
Bu Hana adalah seorang guru pengurus kegiatan ekstrakulikuler yang ada
di sekolahnya. Ia meminta perwakilan dari setiap ekstrakulikuler untuk
mengisi data siswa yang tergabung di dalam ekstrakulikulernya. Setiap
murid hanya diperbolehkan mengikuti satu ekstrakulikuler.
a. Dalam satu ekstrakulikuler tidak boleh ada nama yang berulang
b. Ada tiga kategori; Olahraga (Tenis), Bahasa (English Club),
   dan Seni (Paduan Suara.

'''
while True:
    print("Daftar Murid Sesuai Ekstrakulikuler")
    print("1. Olahraga")
    print("2. Bahasa")
    print("3. Seni")
    print("4. EXIT")
    data = {"Olahraga": "Tenis",
            "Bahasa": "English Club",
            "Seni": "Paduan Suara"}
    user = int(input("Pilih golongan ekstrakulikuler Anda: "))
    if user == 1:
        hasil = data.get('Olahraga')
        nama_ekstra = input("Masukkan nama ekstrakulikuler: ")
        if nama_ekstra in hasil:
           nama_anggota = input("Masukkan nama anggota: ")
           unik = nama_anggota.split()
           print(set(unik))
        else:
            print("Ekstrakulikuler tidak tersedia")
            continue
    if user == 2:
        hasil_2 = data.get('Bahasa')
        nama_ekstra_2 = input("Masukkan nama ekstrakulikuler: ")
        if nama_ekstra_2 in hasil_2:
            nama_anggota_2 = input("Masukkan nama anggota: ")
            unik_2 = nama_anggota_2.split()
            print(set(unik_2))
        else:
            print("Ektrakulikuler tidak tersedia")
            continue
    if user == 3:
        hasil_3 = data.get('Seni')
        nama_ekstra_3 = input("Masukkan nama ekstrakulikuler: ")
        if nama_ekstra_3 in hasil_3:
            nama_anggota_3 = input("Masukkan nama anggota: ")
            unik_3 = nama_anggota_3.split()
            print(set(unik_3))
        else:
            print("Ekstrakulikuler tidak tersedia")
            continue
    if user == 4:
        print("Anda telah keluar dari program")
        break
    else:
        break



