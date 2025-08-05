import re
def check_password(psw):
    if len(psw) < 8:
        raise Exception("parola en az 7 karakter olmalıdır")
    elif not re.search("[a-z]", psw):
        raise Exception("parola küçük harf içermelidir")
    elif not re.search("[A-Z]", psw):
        raise Exception("parola büyük harf içermelidir")
    elif not re.search("[0-9]", psw):
        raise Exception("parola rakam içermelidir")
    elif not re.search("[_@$]", psw):
        raise Exception("parola özel karakter içermelidir")
    elif re.search("\s", psw):
        raise Exception("parola boşluk içermemelidir")
    else:
        print("geçerli parola")

password = "12345aW$"

try:
    check_password(password)
except Exception as ex:
    print(ex)
else:
    print("geçerli")
finally:
    print("finally")

#Factorial
x = 10
result = 1
for i in range(1,x+1):
    result *=i
