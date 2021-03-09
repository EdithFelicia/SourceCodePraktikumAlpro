# Universitas Kristen Duta Wacana
# Edith Felicia Putri

'''
Anisa ingin membuat sebuah program untuk melihat buku-buku
best seller yang tersedia di toko buku cerita fiksi kecil milik
keluarganya untuk memudahkan pecinta buku bisa menemukan buku
yang mereka inginkan. Berikut keterangan lebih jauh dari program Anisa.

a. Apabila pecinta buku memilih exit, maka pecinta buku diminta untuk
   memilih genre yang tersedia, yaitu Fantasi, Teenfict, dan Horror serta
   menuliskan judul serta jumlah buku yang mereka inginkan.
b. Apabila pecinta buku sudah memilih buku bukan best seller, maka program akan berhenti
c. Buku-buku best seller; Little Magacal Piya, Gemitir, dan Matt and Mou, dengan
   keterangan masing-masingnya: Tersedia, Tidak tersedia, dan Tersedia.
'''

buku = 3
while buku < 4:
    print("=====PROGRAM TOKO BUKU GRAMEDIA======")
    print("Buku BEST SELLER bulan ini!")
    print("1. Little Magacal Piya")
    print("2. Gemitir")
    print("3. Matt and Mou")
    print("4. Lainnya")
    buku = int(input("Masukkan no.buku yang Anda cari: "))
    if buku == 1:
        print("Buku yang Anda cari masih tersedia di palang bertuliskan Fantasious.")
    elif buku == 2:
        print("Mohon maaf stock buku Gemitir sudah habis. Harap datang lagi lain kali.")
    elif buku == 3:
        print("Buku yang Anda cari masih tersedia di palang bertuliskan Loveable")
    elif buku == 4:
        print("Buku yang Anda cari bukan merupakan buku Best Seller.")
        print("Genre Buku")
        print("1. Fantasi")
        print("2. Teenfict")
        print("3. Horror")
        user = int(input("Masukkan genre buku yang Anda cari: "))
        if user == 1 or user == 2 or user == 3:
            judul = input("Judul buku: ")
            jumlah = int(input("Berapa buku yang Anda inginkan: "))
            print("Anda mencari buku ", judul, " dengan jumlah", jumlah)
            print("Silakan menjemput buku Anda di kasir dan lakukan pembayaran. Terima kasih")
            break
        else:
            print("Genre buku yang Anda cari tidak tersedia di toko kami")
            print("Silakan mencari di toko buku lain.")
    else:
        print("Pilihan Anda tidak sesuai dengan no.buku yang tersedia.")






