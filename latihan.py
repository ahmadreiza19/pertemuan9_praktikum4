print("Nama     : Ahmad Reiza")
print("Kelas    : T1.20.B.1")
print("NIM      : 312010037")
print()



print("Membuat list dengan sebanyak 5 elemen")
list_saya=[1, 2, 3, 4, 5]
print(list_saya)

print("Menampilkan elemen ke 3")
print(list_saya[2])

print("Ambil nilai dari elemen ke 2 sampai 4")
print(list_saya[1:4])

print("Ambil elemen terakhir")
print(list_saya[4])

print("Ubah elemen ke 4 dengan nilai lainnya")
list_saya[3] = 6
print(list_saya)

print("Ubah elemen ke 4 sampai dengan elemen terakhir")
list_saya[3:5] = [8, 12]
print(list_saya)

print("Ambil 2 bagian dari list pertama (A) dan jadikan list ke 2 (B)")
data_saya = list_saya[1:3]
print(data_saya)

print("Tambah list B dengan nilai string")
data_saya.extend(["Ahmad"])
print(data_saya)

print("Tambah list B dengan 3 nilai")
data_saya.extend(["Reiza", 19, 5])
print(data_saya)

print("Gabungkan list B dengan list A")
gabungan = data_saya + list_saya
print(gabungan)

