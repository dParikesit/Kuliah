# Program waterjug
# In search of 4 liter of water...


# Fungsi guide
# Print list perintah yang ada beserta isi sekarang
# Fungsi controller
# Mengolah masukan menjadi fungsi
# Fungsi satu
# Mengisi jug kapasitas 3
# Fungsi dua
# Mengisi jug kapasitas 5
# Fungsi tiga
# Mengosongkan jug kapasitas 3
# Fungsi empat
# Mengosongkan jug kapasitas 5
# Fungsi lima
# Memindah isi jug 3 ke jug 5 dengan sisa tetap ada
# Fungsi enam
# Memindah isi jug 5 ke jug 3 dengan sisa tetap ada

# Kamus
# isiSatu   : int
# isiDua    : int
# masukan   : int
# check     : boolean

# Algoritma
isiTiga = 0
isiLima = 0
masukan = 0
check = False

def guide():
    global masukan
    print("Ember 3 liter : ", isiTiga)
    print("Ember 5 liter : ", isiLima)
    print()
    print("Pilih no instruksi")
    print("1. isi ember 3 liter")
    print("2. isi ember 5 liter")
    print("3. Kosongkan ember 3 liter")
    print("4. Kosongkan ember 5 liter")
    print("5. Pindahkan isi ember 3 liter ke 5 liter")
    print("6. Pindahkan isi ember 5 liter ke 3 liter")
    masukan = int(input("Nomor instruksi yang dipilih : "))
    print("------------------------")

def controller(arg1):
    if arg1 == 1:
        return satu()
    elif arg1 == 2:
        return dua()
    elif arg1 == 3:
        return tiga()
    elif arg1 == 4:
        return empat()
    elif arg1 == 5:
        return lima()
    elif arg1 == 6:
        return enam()

def checker():
    global isiTiga
    global isiLima
    if isiLima==4:
        return True
    return False

def satu():
    global isiTiga
    isiTiga = 3

def dua():
    global isiLima
    isiLima = 5

def tiga():
    global isiTiga
    isiTiga = 0

def empat():
    global isiLima
    isiLima = 0

def lima():
    global isiTiga
    global isiLima
    while (isiLima<5):
        if isiTiga==0:
            break
        isiTiga-=1
        isiLima+=1

def enam():
    global isiTiga
    global isiLima
    while (isiTiga<3):
        if isiLima==0:
            break
        isiLima-=1
        isiTiga+=1


print("Selamat datang di simulasi Water Jug")
while check == False:
    guide()
    controller(masukan)
    check = checker()
else:
    print("Selamat Anda telah mendapatkan water jug berisi 4 liter!")

