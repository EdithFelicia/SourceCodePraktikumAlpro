# Edith Felicia Putri
# Universitas Kristen Duta Wacana

'''
Anggi ingin membeli baju seharga Rp 120.000 yang mendapat diskon 15%.
Lalu dia juga ingin membeli sebuah baju dengan model berbeda yang
harganya Rp 200.000, yang harus dibayarkan oleh Anggi adalah sebesar
45% dari harga sebelum diskon. Berapa besar diskon untuk baju dengan
model berbeda itu?

Ref : Soal No. 7
link : https://kabarkan.com/contoh-soal-matematika-kelas-6-sd-semester-1-dan-2/
'''
# Input
harga_baju_1 = int(input("Masukkan harga baju pertama yang dibeli: "))
persenan_diskon_baju_1 = float(input("Masukkan persenan diskon baju pertama yang dibeli: "))
harga_baju_lain = int(input("Masukkan harga baju kedua yang dibeli: "))
persenan_harus_dibayar = float(input("Masukkan berapa persen yang harus dibayar: "))

# PROSES
# ANGGI HARUS MEMBAYAR
harga_sebelum_diskon = harga_baju_1 + harga_baju_lain
anggi_bayar = persenan_harus_dibayar * harga_sebelum_diskon
print("Pengguna harus membayar sebesar", 'Rp', anggi_bayar)

# BESAR DISKON BAJU PERTAMA
besar_diskon_baju_1 = harga_baju_1 * persenan_diskon_baju_1
print("Besar diskon dari baju pertama adalah", 'Rp', besar_diskon_baju_1)

# HARGA BAJU PERTAMA SETELAH DISKON
harga_baju_1_setelah_diskon = harga_baju_1 - besar_diskon_baju_1
print("Harga baju pertama setelah mendapat diskon adalah", 'Rp', harga_baju_1_setelah_diskon)

# HARGA KESELURUHAN YANG DIBAYAR
harga_keseluruhan = harga_baju_1_setelah_diskon + harga_baju_lain
print("Biaya belanja Anggi disertai dengan diskon adalah", 'Rp', harga_keseluruhan)

# HARGA BAJU KEDUA SETELAH DISKON
# anggi_bayar = harga_baju_1_setelah_diskon + harga_baju_lain_setelah_diskon
harga_baju_lain_setelah_diskon = anggi_bayar - harga_baju_1_setelah_diskon
print("Harga baju kedua setelah mendapat diskon adalah", 'Rp', harga_baju_lain_setelah_diskon)

# BESAR DISKON BAJU KEDUA
besar_diskon_baju_lain = harga_baju_lain - harga_baju_lain_setelah_diskon
print("Besar diskon dalam rupiah untuk baju lain adalah", besar_diskon_baju_lain)

# OUTPUT
# PERSENAN DISKON BAJU KEDUA
# besar_diskon_baju_lain = harga_baju_lain * persenan_diskon_baju_lain
persenan_diskon_baju_lain = besar_diskon_baju_lain / harga_baju_lain
print("Persenan diskon dari baju kedua adalah", persenan_diskon_baju_lain)
