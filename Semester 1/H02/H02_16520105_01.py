# NIM/Nama  : 16520105/Dimas Shidqi Parikesit
# Tanggal   : 01 November 2020
# Deskripsi : TP Problem 1, Print 1-N dalam sebaris

# Program Print
# Print angka

# Kamus
# N : int
# i : int

# Algoritma
N = int(input('Masukkan N: '))
for i in range(N):
    if i==N-1:
        # Agar output diakhiri new line (untuk auto judge)
        print(i+1)
    else:
        # Agar antar output dipisahkan spasi, bukan new line
        print(i+1, end=' ')