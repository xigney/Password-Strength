import re

def strength_checker(username, password):
    #Parola sekiz karakterden küçük olmamalı!
    if len(password) < 8:
        return False
    #Parolanın içinde username bulunmamalı
    if re.search(username.lower(), password.lower()):
        return False
    #Parolanın içerisinde boşluk olmamalı
    if re.search("\s", password):
        return False
    #Parolanın içerisinde en az bir tane büyük harf olmalı
    if not re.search(r'[A-Z]', password):
        return False
    #Parolanın içerisinde en az bir tane küçük harf olmalı
    if not re.search(r'[a-z]', password):
        return False
    #Parolanın içerisinde en az bir tane büyük harf olmalı
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    #Ben parolamda veya kullanıcı adımda bu karakterlerin olmasını istemiyorum
    if re.search(r'[#%^&()?{}|]', password) or re.search(r'[#%^&()?{}|]', username):
        return False
    
    #Bütün şartları karşılarsan şifre doğrudur. Tabii ki
    return True

#Kullanıcı Adını Al
user = input("Username: ")
#Parolayı Al
pswd = input("Password: ")

#Kullanıcıdan aldığımız verileri fonksiyonumuza ekleyelim
result = strength_checker(user, pswd)

#Fonksiyonu kullanarak kontrol yapalım
if result:
    print("Strong Password")
else:
    print("Password does not meet requirements.")
    
    