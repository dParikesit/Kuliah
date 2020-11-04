# NIM/Nama  : 16520105/Dimas Shidqi Parikesit
# Tanggal   : 01 November 2020
# Deskripsi : TP Problem 2, tulis eksponen10 terkecil

# Program eksponen
# Mencari bilangan eksponen10 terkecil

# Kamus
# N : int
# x : int -> Kondisi awal 10^0

# Algoritma
n = int(input("Masukkan N: "))
x=0
if n<0:
    # Karena -10<=n<0 menghasilkan 1
    if n>=-10:
        print(10**x)
    else:
        # Untuk tau pangkat berapa
        while n<-1:
            x+=1
            n = n//10
        print(-1*(10**(x-1)))
elif n>0:
    # Karena jika n>0 maka hasil minimumnya 10
    x+=1
    while (n//10 !=0):
        x+=1
        n = n//10
    print(10**(x))
else:
    # Kondisi jika n==0, maka jawaban 1
    print(10**x) 