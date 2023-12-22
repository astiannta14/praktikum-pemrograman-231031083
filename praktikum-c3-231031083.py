nama = 'asti ananta'
nim = '231031083'
meet = 'praktikum (string)'
prodi = 'Sistem Informasi C'
email = 'astiananta883@gmail.com'
ttl = 'matakali,14-agustus-2005'
alamat = 'jalan jendral sudirman'
asal = 'parepare'
hobi = 'memasak'
tinggi = '155'
print("-"*110)
strl= "asti ananta"


sp = 40
print('-'*sp)
print(nama.upper().center(sp))
print(nim.center(sp))
print('\n'*2)
print(meet.rjust(sp))
print(prodi.rjust(sp))
print(email.lower().rjust(sp))
print('_'*sp)


print(f"""\tHalo,nama saya {nama} dengan nim {nim} dari prodi {prodi} ini adalah file {meet} Teima Kasih.""")
print()
print(f"""Biodata saya,
Nama\t: {Nama} 
Nim\t: {Nim}    
Prodi\t: {Prodi}
TTL\t: {TTL} 
Alamat\t: {Alamat}
Asal\t: {Asal}    
Hobi\t: {Hobi}
Tinggi\t: {Tinggi}cm
      """)




