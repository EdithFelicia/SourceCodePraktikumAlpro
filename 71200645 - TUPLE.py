# Universitas Kristen Duta Wacana
# Edith Felicia Putri

'''
Andi ingin membuat sebuah data Tuple berisi daftar game
online yang dimainkan oleh teman-teman sekelasnya sebagai
survey sederhana, ia juga meminta rating dari game tersebut
menurut teman-temannya. Bantulah Andi untuk menyelesaikan
program yang diinginkannya.

'''

print("========DAFTAR GAME ONLINE========")
print("Menyimpan data game online dan ratingnya")
print("Menampilkan data game online dan ratingnya")
daftar = []
rating = []
urutan = 0
while True:
    nama = input("Masukkan nama: ")
    game = input("Masukkan game kesukaanmu: ")
    daftar.append(game)
    rate = float(input("Masukkan rating game: "))
    rating.append(rate)
    game_lagi = input("Anda ingin menambah game lagi? ")
    if game_lagi == 'yes':
        continue
    if game_lagi == 'no':
        break
    else:
        break

for game in range(len(daftar)):
    print("Game: " + daftar[urutan] + ", rating: ", rating[urutan])
    urutan = urutan + 1

tipe = tuple(daftar)
tipe2 = tuple(rating)

print(type(tipe))
print(type(tipe2))
