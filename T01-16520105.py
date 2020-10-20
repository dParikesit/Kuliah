# Tugas 1
print('This is password registration form.')
print('Your password must consist of mixed case of alphabet without any number, and have a length of 8 characters')
def checker(args):
    if len(args)!=8 | args.islower() | args.isupper():
        return False
    else:
        for char in args:
            if(char.isalpha()==False):
                return False
        return True

pass1 = input('Please input password! ')
while checker(pass1)==False:
    pass1 = input('Please try again! ')
else:
    print('Password registered!')

# Tugas 2 - Pada tugas ini, pass1 
def login(args):
    if args==pass1:
        print('Welcome!')
    else:
        login(input('Please try again! '))

print('This is login form. Please login using password that you just registered.')
login(input('Please input your pass1! '))


