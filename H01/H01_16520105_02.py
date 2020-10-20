# NIM/Nama  : 16520105/Dimas Shidqi Parikesit
# Tanggal   : 18 Oktober 2020
# Deskripsi : TP Problem 2, simple calculator"

# Program calc
# Berfungsi untuk mengolah input dan menghitungnya

# Kamus
# operand1 : int
# operand2 : int
# operator : string

# Algoritma
operand1 = int(input("Masukkan angka pertama: "))
operand2 = int(input("Masukkan angka kedua: "))
operator = input("Masukkan operator: ")

def calc (arg1, arg2, arg3):
    if arg3 == '+':
        return arg1 + arg2
    elif arg3 == '-':
        return arg1 - arg2
    elif arg3 == '*':
        return arg1 * arg2
    elif arg3 == '/':
        return arg1 // arg2
    elif arg3 == '%':
        return arg1 % arg2

print(str(operand1) + " " + operator + " " +str(operand2) + " = " + str(calc(operand1, operand2, operator)))