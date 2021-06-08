# Universitas Kristen Duta Wacana
# 71200645 - Edith Felicia Putri

'''
Andi memiliki kalimat berisi nama dan umur dan ingin menyimpannya di dalam
dictionary. Sebelum itu dia harus memasukkan pass terlebih dahulu untuk
bisa menyimpan kalimat tersebut.
a. Pass = 10041892
b. Kalimat = Naren berusia 12 tahun, Kirana berusia 23 tahun. Oscar berusia 20 tahun, Elina berusia 45 tahun
c. Kalimat = Kiliana   berusia32tahun, Anjani-berusia32 tahun. Angkasa berusia-10tahun, Rina*berusia 19 tahun

'''
import re
password = input("Masukkan password: ")
data_password = "10041892"
cari = re.search(r"[0-9]",password)
while data_password != password:
    print("PASSWORD ANDA SALAH")
    break
else:
    print("SILAKAN MASUK")
    print(" ")
    kata = input("Masukkan kalimat: ")
    umur = re.findall(r"\d{1,2}",kata)
    nama = re.findall(r"[A-Z][a-z]*",kata)

    umurDict = {}
    urutan = 0
    for setiap_nama in nama:
        umurDict[setiap_nama] = umur[urutan]
        urutan = urutan + 1
    print(umurDict)