# Program
# Menerima banyaknya data yang dihitung (n). Kemudian masukkan n buah data. Kemudian mengeluarkan rata-rata nya

# Kamus
# n : int
# sum : int -> dimulai dari 0
# mean : int

# Algoritma
n=int(input("Masukkan banyaknya data = "))
while n<=0:
    print("Masukan salah. Ulangi.")
    n=int(input("Masukkan banyaknya data = "))

sum=0
print("Data ketinggian tanah = ")
for i in range(n):
    sum+=int(input())
mean = sum/n
print("Rata-rata ketinggian tanah = ", round(mean, 2))
