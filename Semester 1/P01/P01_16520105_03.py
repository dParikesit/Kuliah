# NIM/Nama  : 16520105/Dimas Shidqi Parikesit
# Tanggal   : 21 Oktober 2020
# Deskripsi : Problem 3, Tuan Mor Kin Ryo

# Kamus
# x0    : int
# y0    : int
# x1    : int
# x2    : int
# x3    : int
# y1    : int
# y2    : int
# y3    : int
# dist1 : int
# dist2 : int
# x01, y01 : int
# x12, y12 : int
# x23, y23 : int
# x02, y02 : int
# x13, y13 : int

# Algoritma
x0 = 0
y0 = 0
x1 = int(input("Masukkan x1: "))
y1 = int(input("Masukkan y1: "))
x2 = int(input("Masukkan x2: "))
y2 = int(input("Masukkan y2: "))
x3 = int(input("Masukkan x3: "))
y3 = int(input("Masukkan y3: "))

# Karena restoran harus terakhir, maka kemungkinan hanya 0123 (dist1)
# atau 0213 (dist2)
if x0 < x1:
    x01 = x1-x0
else:
    x01 = x0-x1

if y0 < y1:
    y01 = y1-y0
else:
    y01 = y0-y1

if x1 < x2:
    x12 = x2-x1
else:
    x12 = x1-x2

if y1 < y2:
    y12 = y2-y1
else:
    y12 = y1-y2

if x2 < x3:
    x23 = x3-x2
else:
    x23 = x2-x3

if y2 < y3:
    y23 = y3-y2
else:
    y23 = y2-y3

if x0 < x2:
    x02 = x2-x0
else:
    x02 = x0-x2

if y0 < y2:
    y02 = y2-y0
else:
    y02 = y0-y2

if x1 < x3:
    x13 = x3-x1
else:
    x13 = x1-x3

if y1 < y3:
    y13 = y3-y1
else:
    y13 = y1-y3

dist1 = (x01+y01)+(x12+y12)+(x23+y23)
dist2 = (x02+y02)+(x12+y12)+(x13+y13)

if dist1>dist2:
    print("Jarak terpendeknya adalah "+ str(dist2) + ".")
else:
    print("Jarak terpendeknya adalah "+ str(dist1) + ".")