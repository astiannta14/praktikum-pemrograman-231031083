print('praktikum-1')
print()
print('Nama Lengkap : ASTI ANANTA')
print('NIM          : 231031083')
print('Prodi        : Sistem Informasi C')        

angkatan = 2023
print('Angkatan adalah',angkatan)
print()
a = 20
print('Data adalah = ',a)
print('Tipe data adalah =',type(a))

print()
b = 20.0
print('Data adalah =',b)
print('Tipe data adalah =',type(b))

print()
kampus = 'Institut Teknologi BJ Habibie'
print('Data adalah =',kampus)
print('Tipe data adalah =',type(kampus))

print()
log = True
print('Data adalah =',log)
print('Tipe data adalah =',type(log))

print()
c = complex(3,4)
print('Data adalah =',c)
print('Tipe data adalah =',type(c))
print()
p = 20
q = 5
hasil = p + q
print('hasil',p,'+',q,'=',hasil)
print()
p = 20
q = 5
hasil = p - q
print('hasil',p,'-',q,'=',hasil)
print()
p = 20
q = 5
hasil = p * q
print('hasil',p,'*',q,'=',hasil)
print()
p = 20
q = 5
hasil = p / q
print('hasil',p,'/',q,'=',hasil)
print()
p = 20
q = 5
hasil = p % q
print('hasil',p,'%',q,'=',hasil)
print()
p = 20
q = 5
hasil = p ** q
print('hasil',p,'**',q,'=',hasil)
print()
p = 20
q = 5
hasil = p // q
print('hasil',p,'//',q,'=',hasil)

print()
a = 20
print("nilai a adalah",a)
a = a + 1           #ini perintah  a = a + 1
print("nilai a menjadi",a)


a = 25
print("nilai a adalah",a)
a -= 2           #ini perintah  a = a - 2
print("nilai a-=2 menjadi",a)


a = 20
print("nilai a adalah",a)
a *= 2           #ini perintah  a = a * 2
print("nilai a*=2 menjadi",a)


a = 20
print("nilai a adalah",a)
a /= 5           #ini perintah  a = a / 5
print("nilai a/=5 menjadi",a)


a = 20
print("nilai a adalah",a)
a **= 5           #ini perintah  a = a ** 5
print("nilai a**=5 menjadi",a)


a = 20
print("nilai a adalah",a)
a %= 7           #ini perintah  a = a % 7
print("nilai a%=7 menjadi",a)

a = 20
print("nilai a adalah",a)
a //= 7           #ini perintah  a = a // 7
print("nilai a//=7 menjadi",a)

print() #ini operasi OR
log = True
print("nilai log adalah",log)
log |= False #ini perintah log = log | false
print("nilai log|=False adalah",log)

print() #ini operasi AND
log = True
print("nilai log adalah",log)
log &= False #ini perintah log = log & false
print("nilai log&=False adalah",log)

print() #ini operasi XOR
log = True
print("nilai log adalah",log)
log ^= True #ini perintah log = log ^ True
print("nilai log ^=True adalah",log)

print() # ini operasi shift king
bi = 0b0100
print("nilai bi =",format(bi,'04b'))
bi >>= 1 #menggeser digit ke kanan 1 kali
print("nilai bi >>=",format(bi,'04b'))

print()
a = 20
hasil = a>1 # lebih dari
print("hasil",a,'>15 adalah', hasil)

a = 20
hasil = a<5 # kurang dari
print("hasil",a,'<5 adalah', hasil)

print()
y = 20
hasil = a==1 #sama dengan (bukan pemberi nilai)
print("hasil",a,'==20 adalah', hasil)

y = 30
hasil = a!=5 # tidak sama dengan
print("hasil",a,'!=30 adalah', hasil)

y = 20
hasil = a>=2 # lebih dari sama dengan
print("hasil",a,'>= adalah', hasil)

y = 30
hasil = a<=3 # kurang dari sama dengan
print("hasil",a,'<=35 adalah', hasil)
