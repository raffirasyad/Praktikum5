# Import Package Tabulate
from tabulate import tabulate

# Membuat list kosong untuk menampung data 
dataMahasiswa = []
no = 0

# melakukan perulangan input sesuai dengan keinginan sampai pertanyaan tambah data dimunculkan kembali
while(True):

# membuat variable untuk menampung inputan
    no +=1

    nama = input(" Masukan Nama :  ")
    nim = input("Masukan Nim:  ")
    kelas = input("Masukan Kelas:  ")
    matkul = input("Masukan Mata Kuliah:   " )

# mengkonversi string ke integer
    tugas = int(input("Masukan Nilai Tugas : "))
    uts = int(input("Masukan Nilai UTS : "))
    uas = int(input("Masukan Nilai UAS : "))

# menjumlahkan nilai dari tugas,uts dan uas
    nilai_akhir = (tugas * 30 / 100) + (uts * 35 / 100) + (uas * 35 / 100)

 # menambahkan data input ke list dataMahasiswa  
    dataMahasiswa.append(
    [no, nama, nim, kelas, matkul, tugas, uts, uas, nilai_akhir])
# input tambah data jika tekan y maka input kembali, selain itu berhenti dan tampilkan data   
    tambah_data_lagi = input("Tambah Data lagi ? (y/t) : ")
    if(tambah_data_lagi == "t"):
        break
# tampilkan dataMahasiswa menggunakan tabulate package agar tampilan berbentuk table
print(tabulate(dataMahasiswa, headers=[
      "No", "Nama", "Nim", "Kelas", "Mata Kuliah", "Tugas", "UTS", "UAS", "Nilai Akhir"], tablefmt="fancy_grid"))
