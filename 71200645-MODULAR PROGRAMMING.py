# Universitas Kristen Duta Wacana
# Edith Felicia Putri

'''
Marina membuka toko buah sederhana dan kecil bersama Ibunya.
Untuk sementara ini, ia akan menjual Apel, Jeruk, dan Semangka.
Dengan harga Rp8.000, Rp10.000, dan Rp25.000 masing-masingnya.
Sebagai awal, ia juga memberi diskon sebesar 15% untuk setiap
pembelian Apel dan 5% untuk Semangka.

Ibunya kurang pandai dalam hitung-menghitung, dan ia hendak
membantu Ibunya dengan membuatkan program mudah agar Ibunya
tidak harus menghadapi pelanggan dan hanya menerima uang
sesuai jumlah yang ditampilkan program Marina.
'''

def hargaBeli(jumlah, harga, diskon=0):
    bayar = (harga - (harga * diskon/100)) * jumlah
    return bayar

print("=====TOKO BUAH MARINA=====")
nama = input("Nama Anda: ")
print("Kami menjual buah-buahan sebagai berikut: ")
print("1. Apel")
print("2. Jeruk")
print("3. Semangka")
pilihan = int(input("Hari ini " + nama + " ingin membeli apa?"))

if pilihan == 1:
    harga = 8000
    diskon = 15
    jumlah = int(input("Masukkan berapa buah yang Anda inginkan: "))
    seluruh_bayar = hargaBeli(jumlah, harga, diskon)
    print("Anda harus membayar sebesar Rp", seluruh_bayar)
elif pilihan == 2:
    harga = 10000
    jumlah = int(input("Masukkan berapa buah yang Anda inginkan: "))
    seluruh_bayar = hargaBeli(jumlah, harga)
    print("Anda harus membayar sebesar Rp", seluruh_bayar)
else:
    harga = 25000
    diskon = 5
    jumlah = int(input("Masukkan berapa buah yang Anda inginkan: "))
    seluruh_bayar = hargaBeli(jumlah, harga, diskon)
    print("Anda harus membayar sebesar Rp", seluruh_bayar)
    
print("Terima kasih! Silakan datang lagi lain kali!")
