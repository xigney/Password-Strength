import re
import os
from platform import system
import sys
import time
import pyfiglet

def clear():
    if system() == 'Linux':
        os.system("clear")
    if system() == 'Windows':
        os.system('cls')
        os.system('color a')
    else:
        pass
    
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2. / 100)

def slowprint2(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.20 / 100)

def slowprint3(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.04 / 100)
        
def strength_checker(username, password):
    #Parola sekiz karakterden küçük olmamalı!
    if len(password) < 8:
        return False
    #Parolanın içinde username bulunmamalı
    if re.search(username.lower(), password.lower()):
        return False
    #Parolanın içerisinde boşluk olmamalı
    if re.search("/s", password):
        return False
    #Parolanın içerisinde en az bir tane büyük harf olmalı
    if not re.search(r'[A-Z]', password):
        return False
    #Parolanın içerisinde en az bir tane küçük harf olmalı
    if not re.search(r'[a-z]', password):
        return False
    #Parolanın içerisinde en az bir tane sayı olmalı
    if not re.search(r'[1-9]', password):
        return False
    #Parolanın içerisinde en az bir tane büyük harf olmalı
    if not re.search(r'[!@$*,.]', password):
        return False
    #Ben parolamda veya kullanıcı adımda bu karakterlerin olmasını istemiyorum
    if re.search(r'[#%^&()?{}|<>:"]', password) or re.search(r'[#%^&()?{}|<>:"]', username):
        return False
    
    #Bütün şartları karşılarsan şifre doğrudur. Tabii ki
    return True
        
clear()
        
ASCII_art_1 = pyfiglet.figlet_format("xigney")
print("\033[38;5;197m")
slowprint(ASCII_art_1)     

#Kullanıcı Adını Al
user = input("Username: ")
#Parolayı Al
pswd = input("Password: ")

clear()

#Kullanıcıdan aldığımız verileri fonksiyonumuza ekleyelim
result = strength_checker(user, pswd)

#Bu renk kırmızı!
print("\033[38;5;197m")
slowprint(f"### Username: {user}")
slowprint(f"### Password: {pswd}\n")

#Fonksiyonu kullanarak kontrol yapalım
if result:
    #Bu renk yeşil!
    slowprint("\033[1;92mStrong Password")
else:
    slowprint("\033[1;92mPassword does not meet requirements.")
    
    