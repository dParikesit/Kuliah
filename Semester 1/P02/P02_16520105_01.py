# NIM/Nama  : 16520105/Dimas Shidqi Parikesit
# Tanggal   : 04 November 2020
# Deskripsi : Problem 1, Keterbagian

# Program
# Loop 1-N dengan tiap digit diolah seperti berikut
# Jika x kelipatan A, keluarkan "Siap"
# Jika x kelipatan B, keluarkan "Bang"
# Jika x kelipatan C, keluarkan "Jago"

# Kamus
# N : int
# A : int
# B : int
# C : int
# x : int

# Algoritma
N = int(input("Masukkan nilai N: "))
A = int(input("Masukkan nilai A: "))
B = int(input("Masukkan nilai B: "))
C = int(input("Masukkan nilai C: "))

for x in range(N):
    # Pakai if banyak, dan bukan if elif agar jika bisa dibagi sekaligus bisa print semuanya
    # end='' agar jika bisa dibagi sekaligus tidak akan berspasi
    if (x+1)%A==0:
        print("Siap", end='')
    if (x+1)%B==0:
        print("Bang", end='')
    if (x+1)%C==0:
        print("Jago", end='')
    if ((x+1)%A!=0)&((x+1)%B!=0)&((x+1)%C!=0):
        print((x+1), end='')
    
    # untuk memastikan antar output tiap angka ada spasinya
    print(' ',end='')