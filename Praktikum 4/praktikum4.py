data_mahasiswa = []

while True:
    print("Input Data Mahasiswa")
    name = input("Nama        : ")
    nim = input("NIM         : ")
    tugas = float(input("Nilai Tugas : "))
    uts = float(input("Nilai UTS   : "))
    uas = float(input("Nilai UAS   : "))

    nilai_akhir = (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)

    data_mahasiswa.append([name, nim, tugas, uts, uas, nilai_akhir])

    lagi = input("Tambahkan data lagi? (ya/tidak): ")
    if lagi.lower() == "tidak":
        break

print("=" * 65)
print(f"| {'NO':^2} | {'NAMA':^10} | {'NIM':^9} | {'TUGAS':^5} | {'UTS':^4} | {'UAS':^4} | {'AKHIR':^9} |")
print("=" * 65)

no = 1
for mhs in data_mahasiswa:
    print(f"| {no:^3}| {mhs[0]:^10} | {mhs[1]:^8} | {mhs[2]:^5} | {mhs[3]:^3} | {mhs[4]:^3} | {mhs[5]:^8.1f}  |")
    no += 1
print("=" * 65)
