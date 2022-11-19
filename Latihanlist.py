#   Buat sebuah list sebanyak 5 elemen dengan nilai bebas
list_matkul = ["Pemograman","Algoritma","PAI","Medsos","PTI"]

# Tampilkan nilai list ke 3
print(list_matkul[2])

# ambil nilai elemen ke 2 sampai elemen ke 4
print(list_matkul[1:4])

# ambil elemen terakhir
print(list_matkul[4])

# mengubah elmen list ke 4
list_matkul[3] = "Pancasila"
print(list_matkul)

# ubah elemen ke 4 sampai dengan elemen terakhir
list_matkul[3:5] = "Pancasila","B. Indonesia"
print(list_matkul)

# tambah elemen list
# ambil 2 bagian dari list pertama (A) dan jadikan list ke 2 (B)
list_matkul2 = list_matkul [0:2]
print(list_matkul2)

# tambah list_matkul2 dengan nilai string
list_matkul2.append("Medsos")
print(list_matkul2)

# tambah list B dengan 3 nilai
list_matkul2.extend(["B. Indonesia","PTI","PAI"])
print(list_matkul2)

# gabungkan list matkul 2 dengan list matkul 1
list_gabungan = list_matkul2 + list_matkul
print(list_gabungan)
