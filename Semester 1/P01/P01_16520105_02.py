# NIM/Nama  : 16520105/Dimas Shidqi Parikesit
# Tanggal   : 21 Oktober 2020
# Deskripsi : Problem 2, Tuan Mor Integral

# Kamus
# a     : int
# b     : int
# aInt  : int
# bInt  : int

# Algoritma
a = int(input("Masukkan a: "))
b = int(input("Masukkan b: "))

# Seperti yang kita ketahui, integral ax+b adalah (a/2)x^2+bx+C
if a%2 == 0:
    aInt = int(a/2)
else:
    aInt = a/2
bInt = b

if aInt == 1:
    # Jika aInt == 1, maka tidak perlu ditulis aInt nya
    print("Integral dari f(x) adalah x^2+"+str(bInt)+"x+C")
else:
    print("Integral dari f(x) adalah "+str(aInt)+"x^2+"+str(bInt)+"x+C")
