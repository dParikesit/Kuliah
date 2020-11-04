# NIM/Nama  : 16520105/Dimas Shidqi Parikesit
# Tanggal   : 18 Oktober 2020
# Deskripsi : TP Problem 3, integer checker"

# Program checker
# Berfungsi untuk menentukan apakah sebuah bilangan positif ganjil, positif genap,
# negatif, atau nol.

# Kamus
# x : int

# Algoritma
x = int(input("Masukkan X: "))

def checker(arg):
    if arg < 0:
        print("X adalah bilangan negatif")
    elif arg > 0:
        if(arg % 2 == 0):
            print("X adalah bilangan positif genap")
        else:
            print("X adalah bilangan positif ganjil")
    else:
        print("X adalah bilangan nol")

checker(x)