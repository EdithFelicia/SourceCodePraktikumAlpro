# Universitas Kristen Duta Wacana
# 71200645 - Edith Felicia Putri

'''
Indiana ingin membuat daftar impian yang ingin dikunjunginya
sambil menunggu hari ulang tahunnya pada waktu tengah malam.
Buatlah dengan fungsi rekursif perhitungan mundur dan
harapan-harapan Indiana.
'''

def tanya_mundur(num):
    simpan = []
    if (num == 0):
        print(" ")
        print("SELAMAT ULANG TAHUN YANG KE-",umur,nama)
        print(" ")
    else:
        print(num)
        tanya = input("Impian: ")
        next_num = num - 1
        tanya_mundur(next_num)
        simpan.append(tanya)
        print("SEMOGA IMPIANMU TERWUJUD!")
        print(simpan)
    return " "

nama = input("Masukkan nama: ")
umur = int(input("Masukkan umur: "))
angka = int(input("Masukkan waktu: "))
print(tanya_mundur(angka))
