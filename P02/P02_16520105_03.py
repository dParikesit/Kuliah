# NIM/Nama  : 16520105/Dimas Shidqi Parikesit
# Tanggal   : 04 November 2020
# Deskripsi : Problem 3, Pola generator

# Program
# Diberikan N, gambar menggunakan angka 0 berukuran 2N*2N
# gambar kotak lebih kecil menggunakan angka 1
# lakukan sampai selesai menggambar angka N-1
# Jika N>=0, tulis satuannya saja

# Kamus
# N : int
# i : int -> index looping
# j : int -> index looping
# k : int -> index looping
# x : int -> variabel sementara jika >=10

# Algoritma
N=int(input("Masukkan bilangan: "))
print("Pola yang terbentuk: ")

# Gambar pola setengah atas
for i in range(N):
    # Gambar setengah kiri
    for j in range(i+1):
        if j>=10:
            x=j
            while x>=10:
                x%=10
            print(x, end='')
        else:
            print(j, end='')
    
    # Gambar tengah yang berlebih
    k=i
    while k<N-1:
        if i>=10:
            x=i
            while x>=10:
                x%=10
            print(x, end='')
            print(x, end='')
        else:
            print(i, end='')
            print(i, end='')
        k+=1
    
    # Gambar setengah kanan
    for j in range(i, -1, -1):
        if j>=10:
            x=j
            while x>=10:
                x%=10
            print(x, end='')
        else:
            print(j, end='')
    print()

# Gambar pola setengah bawah
for i in range(N-1, -1, -1):
    # Gambar setengah kiri
    for j in range(i+1):
        if j>=10:
            x=j
            while x>=10:
                x%=10
            print(x, end='')
        else:
            print(j, end='')

    #Gambar yang berlebih
    k=i
    while k<N-1:
        if i>=10:
            x=i
            while x>=10:
                x%=10
            print(x, end='')
            print(x, end='')
        else:
            print(i, end='')
            print(i, end='')
        k+=1

    # Gambar setengah kanan
    for j in range(i, -1, -1):
        if j>=10:
            x=j
            while x>=10:
                x%=10
            print(x, end='')
        else:
            print(j, end='')
    print()
    
