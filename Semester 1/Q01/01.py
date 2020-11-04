# Program
# Mendapatkan input n, V dan T untuk menghitung P

# Kamus
# p : float karena bisa koma
# v : float karena bisa koma
# n : float karena bisa koma
# r : constant (float karena pasti koma)
# t : float karena bisa koma

# Algoritma
R = 8.314
v = float(input("Masukkan V dalam meter-kubik: "))
while v==0:
    print("V tidak boleh 0")
    v=float(input("Masukkan V dalam meter-kubik: "))
t = float(input("Masukkan T dalam Kelvin: "))
n = float(input("Masukkan jumlah mol: "))

p = (n*R*t)/v
print("Tekanan sebesar",p,"pascal")