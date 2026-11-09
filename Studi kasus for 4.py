## Dosen memasukkan nilai 5 mahasiswa. Mahasiswa dinyatakan lulus jika nilainya minimal 65.
## Program menghitung jumlah mahasiswa yang lulus.

nilai_mahasiswa = []
jumlah_mahasiswa_lulus = int()

for mahasiswa in range(1,6):
    nilai_mahasiswa_individu = int(input(f"Masukkan nilai mahasiswa {mahasiswa}: "))
    nilai_mahasiswa.append(nilai_mahasiswa_individu)

    if nilai_mahasiswa_individu >= 65:
        jumlah_mahasiswa_lulus += 1

print(f"Jumlah mahasiswa lulus: {jumlah_mahasiswa_lulus}")
