# Universitas Kristen Duta Wacana
# Edith Felicia Putri

'''
Andi ingin membuat sebuah data Tuple berisi daftar game
online yang dimainkan oleh teman-teman sekelasnya sebagai
survey sederhana, ia juga meminta rating dari game tersebut
menurut teman-temannya. Bantulah Andi untuk menyelesaikan
program yang diinginkannya.

'''

print("========DATA GAME ONLINE========")
print("Menyimpan data game dan rating")
print("Menampilkan data game dan rating")
daftar =[]
rating = []
urutan = 0
while True:
    print(" ")
    nama = input("Masukkan nama: ")
    data = input("Masukkan game kesukaanmu: ")
    rate = int(input("Masukkan rating " + data + ":"))
    rating.append(rate)
    daftar.append(data)
    data_lagi = input("Anda ingin meminta data lagi? ")
    if data_lagi == 'yes':
        continue
    if data_lagi == 'no':
        break
    else:
        break

for game in range(len(daftar)):
    print("Game: " + daftar[urutan] + ", rating:", rating[urutan])
    urutan = urutan + 1

tipe = tuple(daftar)
tipe2 = tuple(rating)

print(type(daftar))
print(type(rating))