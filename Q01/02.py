# Program
# Menerima masukan 3 bilangan real, mengeluarkan kalimat mungkin membentuk segitiga atau tidak

# Kamus
# a : int
# b : int
# c : int
# max : int -> untuk menyimpan nilai yang maksimum
# mungkin : boolean -> untuk menyimpan apakah mungkin. Dimulai True

# Algoritma
a = int(input("Masukkan bilangan a: "))
b = int(input("Masukkan bilangan b: "))
c = int(input("Masukkan bilangan c: "))
mungkin = True

# Mustahil jika ada yang negatif atau <=0
if (a<=0)|(b<=0)|(c<=0):
    mungkin = False

# Cari max number nya
max = a
if b>max:
    max=b

if c>max:
    max=c

# Hitung apakah memenuhi syarat
if max>=(a+b+c-max):
    mungkin = False

# Print
if mungkin==True:
    print("Ketiga bilangan dapat membentuk segitiga")
else:
    print("Ketiga bilangan tidak dapat membentuk segitiga")
