print("Nama          :Asti Ananta")
print("Nim           :231031083")
print("prodi         :Sistem Informasi C")
print("Tanggal Lahir :14-08-2005")
#operator penugasan
print()
a =14
a +=1
print ('Nilai a +=1 akan menjadi',a)
a =14
a -=1
print ('Nilai a -=1 akan menjadi',a)
a =14
a *=2
print ('Nilai a *=2 akan menjadi',a)
a =14
a /=2
print ('Nilai a /=2 akan menjadi',a)
a =14
a %=2
print ('Nilai a %=2 akan menjadi',a)
a =14
a //=2
print ('Nilai a //=2 akan menjadi',a )
a =14
a **=2
print ('Nilai a **=2 akan menjadi',a )
#OR
b = True
print ('Nilai b =',b )
b |= False
print ('Nilai b|= False akan menjadi',b )
b = False
print ('Nilai b =',b )
b |= False
print ('Nilai b|= False akan menjadi',b )
# AND
b = True
print ('Nilai b =',b )
b &= False
print ('Nilai b&= False akan menjadi',b )
b = False
print ('Nilai b =',b )
b &= False
print ('Nilai b&= False akan menjadi',b )
# XOR
b = True
print ('Nilai b =',b )
b ^= False
print ('Nilai b^= False akan menjadi',b )
b = False
print ('Nilai b =',b )
b ^= False
print ('Nilai b^= False akan menjadi',b )
# Shifting
c =0b0100
print ('Nilai c =',format (c , '04b') )
c >>=1
print ('Nilai c > >=1 akan menjadi ',format (c , '04b') )
c =0b0100
c <<=1
print ('Nilai c < <=1 akan menjadi ',format (c , '04b') )
#operator Komparasi/Perbandingan
a =3 # isi dengan ujung NIM
b =8 # Ubah dengan hasil jumlah ujung NIM dengan 5
print (' ================== Besar dari 8 ’)
hasil = a >8
print (a ,'> 8 adalah ’, hasil )
hasil = b >8
print (b ,'>8 adalah ’, hasil )
print (' ================== Kecil dari 8 ’)
hasil = a <8
print (a ,'< 8 adalah ’, hasil )
hasil = b <8
print (b ,'< 8 adalah ’, hasil )
print (' ================== Besar atau sama dari 8 ’)
hasil = a >=8
print (a ,' >= 8 adalah ’, hasil )
hasil = b >=8
print (b ,' >= 8 adalah ’, hasil )
print (' ================== Besar atau sama dari 8 ’)
hasil = a <=8
print (a ,' <= 8 adalah ’, hasil )
hasil = b <=8
print (b ,' <= 13 adalah ’,< hasil )
print (' ================== Sama dengan 8 ’)
hasil = a ==8
print (a ,'== 8 adalah ’, hasil )
hasil = b ==8
print (b ,'== 8 adalah ’, hasil )
print (' ================== Tidak sama dengan 8 ’)
hasil = a !=8
print (a ,'!= 8 adalah ’, hasil )
hasil = b !=8
print (b ,'!= 8 adalah ’, hasil )
#0perator Logika
print (' ============= NOT ============= ’)
a = True
c = not a
print ('a adalah ’,a )
print (' ------c = not a- - - -- - - NOT ’)
print ('c adalah ’,c )
print (' ============= OR ============= ’)
a = True
b = True
c = a or b
print (a ,'OR ’,b ,’menjadi ’,c )
a = True
b = False
c = a or b
print (a ,'OR ’,b ,’menjadi ’,c )
a = False
b = True
c = a or b
print (a ,'OR ’,b ,’menjadi ’,c )
a = False
b = False
c = a or b
print (a ,'OR ’,b ,’menjadi ’,c )
print (' ============= AND ============= ’)
a = True
b = True
c = a and b
print (a ,'AND ’,b ,’menjadi ’,c )
a = True
b = False
c = a and b
print (a ,'AND ’,b ,’menjadi ’,c )
a = False
b = True
c = a and b
print (a ,'AND ’,b ,’menjadi ’,c )
a = False
b = False
c = a and b
print (a ,'AND ’,b ,’menjadi ’,c )
print (' ============= XOR ============= ’)
a = True
b = True
c = a ^ b
print (a ,'^’,b ,’menjadi ’,c )
a = True
b = False
c = a ^ b
print (a ,'^’,b ,’menjadi ’,c )
a = False
b = True
c = a ^ b
print (a ,'^’,b ,’menjadi ’,c )
a = False
b = False
c = a ^ b
print (a ,'^’,b ,’menjadi ’,c )
# TUGAS
# Buat kode untuk masing masing operator berikut
print (’ ============= NAND ============= ’)
print (’ ============= NOR ============== ’)
print (’ ============= NXOR ============= ’)

#Operator Identitas
1 print (' ============== IS ’)
2 a =5
3 b =5
4 print ('Nilai a =’,a ,’Identitas =’,hex (id( a ) ) )
5 print ('Nilai b =’,b ,’Identitas =’,hex (id( b ) ) )
6 hasil = a is b
7 print (’a is b = ’, hasil )
8
9 a =5
10 b =6
11 print (’Nilai a =’,a ,’Identitas =’,hex (id( a ) ) )
12 print (’Nilai b =’,b ,’Identitas =’,hex (id( b ) ) )
13 hasil = a is b
14 print ('a is b = ’, hasil )
15
16 print (' ============== IS NOT ’)
17 a =5
18 b =5
19 print (’Nilai a =’,a ,’Identitas =’,hex (id( a ) ) )
20 print (’Nilai b =’,b ,’Identitas =’,hex (id( b ) ) )
21 hasil = a is not b
22 print (’a is not b = ’, hasil )
23
24 a =5
25 b =6
26 print (’Nilai a =’,a ,’Identitas =’,hex (id( a ) ) )
27 print (’Nilai b =’,b ,’Identitas =’,hex (id( b ) ) )
28 hasil = a is not b
29 print (’a is not b = ’, hasil )   
       
