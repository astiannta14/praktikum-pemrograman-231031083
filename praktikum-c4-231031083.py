data = ('Asti Ananta',2023,'Aktif')
nilai = (90,89,93,97)

print("Nama: "+ data[0])
print("angkatan: ", data[1])
print("status: "+ data[2])

print(f'{data[0]} status aktif: {data[2]}')
print(f'data terbesar adalah : {max(nilai)}')
print(f'data terkecil adalah : {min(nilai)}')
x = sum(nilai)/len(nilai)
print(f'nilai rata rata adalah {x}')
#  Nama Mahasiswa: Asti Ananta
#  Inisial Mahasiswa: A A
#  NIM Asti Ananta: 231031083
#  Program pendidikan Asti Ananta: S1-Reguler Sistem Informasi C 
#  Angkatan Asti Ananta: Ganjil-2023
#  Total sks Asti Ananta: 11
#  Jumlah nilai Asti Ananta: 5
#  Data terbesar ASti Ananta adalah: 100
#  Data terkecil Asti Ananta adalah: 89
#  Rata-rata nilai Asti Ananta adalah: 92.25 
nama = 'Asti Ananta'
nim = '231031083'
program = 'S1-Reguler Sistem Informasi C' 
sks =  [(11)]
data = [(89,90,93,97)]
print(f'Nama Mahasiswa:',nama)
nama_lengkap = "Asti Ananta"
inisial_list = list(map(lambda nama: nama[0],nama_lengkap.split()))
nama_lengkap = "Asti Ananta"
inisial_list = list(map(lambda nama: nama[0],nama_lengkap.split()))
print(''.join(inisial_list))
print(f'Nim Asti Ananta:',nim)
