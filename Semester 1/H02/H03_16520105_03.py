# NIM/Nama  : 16520105/Dimas Shidqi Parikesit
# Tanggal   : 01 November 2020
# Deskripsi : TP Problem 3, Prime testing

# Program Print
# Cek keprimaan menggunakan pembagian angka sebelumnya

# Kamus
# x :int
# i :int
# prime : Boolean -> untuk menyimpan apakah prima atau tidak

# Algoritma
x = int(input('Masukkan X: '))
prime = True
for i in range(2,x):
    if x%i==0:
        prime = False

if prime==False:
    print(x, 'bukan bilangan prima')
else:
    print(x, 'adalah bilangan prima')