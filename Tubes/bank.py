import createPass

print("Selamat Datang di m-Banking")
print("Silahkan registrasi terlebih dahulu")
createPass.register(input("Masukkan username = "), input("Masukkan password = "))

createPass.login(input("Masukkan username = "), input("Masukkan password = "))