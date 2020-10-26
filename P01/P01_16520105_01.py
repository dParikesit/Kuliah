# NIM/Nama  : 16520105/Dimas Shidqi Parikesit
# Tanggal   : 21 Oktober 2020
# Deskripsi : Problem 1, Tuan Kan yang adil tapi ngambil sisa permen anak-anak :(

# Kamus
# a     : int
# b     : int
# c     : int
# d     : int
# divd  : int -> Jumlah permen tiap anak

# Algoritma
a = int(input("Masukkan nilai a: "))
b = int(input("Masukkan nilai b: "))
c = int(input("Masukkan nilai c: "))
d = int(input("Masukkan nilai d: "))

divd = (a+b+c+d)//4
print("Setiap anak akan mendapat "+str(divd)+" permen.")