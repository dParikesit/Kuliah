# NIM/Nama  : 16520105/Dimas Shidqi Parikesit
# Tanggal   : 04 November 2020
# Deskripsi : Problem 2, Tuan Mor belajar FPB

# Program
# Diberikan empat bilangan, cari FPB keempat bilangan tersebut

# Kamus
# pertama     : int
# kedua       : int
# ketiga      : int
# keempat     : int
# fpb         : int
# x           : int
# y           : int

# Algoritma
# Menggunakan algoritma euclidean, diketahui bahwa fpb 2 angka dapat dihitung sebagai berikut
# 1. Jika salah satu angka==0, maka fpb nya angka lainnya
# 2. Jika kedua angka bernilai sama, maka fpb merupakan angka tersebut
# 3. Jika kedua angka !=0, tetapi >0, maka fpb nya sama dengan fpb(angkabesar-angkakecil, angkakecil)
# 4. FPB banyak angka sekaligus merupakan fpb 2 angka kecil yang di fpb oleh angka lain

pertama = int(input("Masukkan bilangan pertama: "))
kedua = int(input("Masukkan bilangan kedua: "))
ketiga = int(input("Masukkan bilangan ketiga: "))
keempat = int(input("Masukkan bilangan keempat: "))
fpb = 1 # base case
x=0 # Variabel menyimpan angka yang sedang difpb
y=0 # Variabel menyimpan angka yang sedang difpb

# FPB angka pertama dan kedua
if pertama<kedua:
    x=pertama
    y=kedua
else:
    x=kedua
    y=pertama

while (x>0) & (y>0):
    if x>y:
        x-=y
    elif x<y:
        y-=x
    else:
        fpb=x
        x=-1
        y=-1
if x==0:
    fpb=y
elif y==0:
    fpb=x

# FPB hasil sebelumnya dengan angka ketiga
if ketiga<fpb:
    x=ketiga
    y=fpb
else:
    x=fpb
    y=ketiga

while (x>0) & (y>0):
    if x>y:
        x-=y
    elif x<y:
        y-=x
    else:
        fpb=x
        x=-1
        y=-1
if x==0:
    fpb=y
elif y==0:
    fpb=x

# FPB hasil sebelumnya dengan angka keempat
if keempat<fpb:
    x=keempat
    y=fpb
else:
    x=fpb
    y=keempat

while (x>0) & (y>0):
    if x>y:
        x-=y
    elif x<y:
        y-=x
    else:
        fpb=x
        x=-1
        y=-1
if x==0:
    fpb=y
elif y==0:
    fpb=x

# Print hasilnya
print("FPB dari keempat bilangan tersebut adalah", fpb)