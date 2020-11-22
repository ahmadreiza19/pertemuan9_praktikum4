# Membuat data list
mahasiswa = []
stop = False
i = 0

#menghisi data list
while not stop:
    nama = input("Nama : ")
    nim = input("NIM : ")
    tugas = input("Nilai Tugas : ")
    UTS = input("Nilai UTS : ")
    UAS = input("Nilai UAS : ")
    nilai_akhir = 0.3 * float(tugas) + 0.35 * float(UTS) + 0.35 * float(UAS)

    mahasiswa.append([nama, nim, tugas, UTS, UAS, nilai_akhir])



    tanya = input("Mau menambahkan lagi? (y/t) : ")
    if tanya == "t":
        stop = True

print("==============================================")
print("| No | Nama | NIM | Tugas | UTS | UAS | Akhir |")
print("==============================================")
for data in mahasiswa:
    i += 1
    print(f"| {i} | {data[0]} | {data[1]} | {data[2]} | {data[3]} | {data[4]} | {data[5]} |")
print("==============================================")