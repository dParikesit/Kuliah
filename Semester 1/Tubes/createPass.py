class credential:
    def __init__(self, password):
        self.password = password
    
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value
        print("Password Set!")

user = {}
def register(username, password):
    global user
    user[username] = credential(password)
    print("Register Successful!")

def login(username, passw):
    global user
    if user[username].password==passw:
        print("Login Successful!")
    else:
        print("Please try again!")
        login(input("Masukkan username = "), input("Masukkan password = "))
    