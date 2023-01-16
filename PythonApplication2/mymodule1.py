from aifc import Error
from math import *
from operator import truediv, truth
from pickle import TRUE
from random import choice
import string
import random
import csv

#def password(p:int):
#    pass=""
#    for i in range(k):
#        t=choice(string.ascii_letters)
#        num=choice([1,2,3,4,5,6,7,8,9,0])
#        t_num=[t,str(num)]
#        pass+=choice(t_num)
#    return pass
def main():
    """Funkcia generiruet login i parol i sohranjaet ih v faile."""
    #Poluchit info o polzovatele
    information=get_info()

    #Na osnove polchennih dannih sgenerirovat login.
    login = get_login(information)
    print("Sgenerirovat dannie:")
    print(f"login - {login}")

    #Sgenerirovat parol
    password = get_password(*parameters)
    print(f"password - {password}")

    #Zapisat info v fail
    save_info(information, login, password)
    print("info zapissana v fail.")
def get_login(information):
    """Funktsia generiruet login na osnovanii dannih o polzovatele."""
    fullname = information['fullname']
    name = fullname.split()
    if len(name)==2:
        name, firstname = name
        shortname = f'{name}_{firstname[0]}'
    else:
        name, firstname, patronymic = name
        shortname = f'{name}_{firstname[0]}{patronymic}'
        login="name"
    return login
A_B_C= 'AaBbCcDdEEFfGgHhIiJjKkLlMmNnPpQqRrSsTtUuVvWwXxYyZz'
NUMBERS = '0123456789'
SYMBOLS = A_B_C + NUMBERS
def get_password(A_B_C, SYMBOLS):
    """Funkcija generiruet parol iz 8 simvolov"""
    #Sgenerirovat parol v cikle s ispolzovaniem global konstant
    repeat = Truepassword=''
    while repeat:
        password = ''
        password += A_B_C[random.randint(0,49)]
        for _ in range (7):
            password += SYMBOLS[random.randint(0,59)]
        repeat = check_password(password)
    return password
def check_password(password):
    """Funktsia proverjaet trebovanie k parolju"""
    #Opredelit peremennie dlja proverki nalicjija v parole cifr,
    #Strocnih i propisnih bukv
    is_digit = False
    is_lower = False
    is_upper = False
    #proverit nalichie v parole trebuemih simvolov
    for symbol in password:
        if symbol.isdigit():
            is_digit = True
        elif symbol.islower():
            is_lower = True
        elif symbol.isupper():
            is_upper = True
    is_not_valid = True
    if is_digit and is_lower and is_upper:
        is_not_valid = False
    return is_not_valid
def get_info():
    """Funktsija poluchajet ot polzovatelei korrektnuju info o polzovatele"""
    #Poluchit dannie o polzovatele i proverit ih na korrektnost vvoda
    try:
        fullname = input('Insert here your name:').split()
        information = {'fullname':fullname}
    except (ValueError):
        #V sluchae oshibki povtoritsja vvod dannih
        print('Dannie vvedeni neverno! vesti zanovo.')
        return Error
    else:
        #Vernut slovar s dannimi
        return information
def save_info(information, login, password):
    fullname = information['fullname']
    w_info = [fullname]
    cur_datetime = datetime.now()
    w_datetime = f'{cur_datetime.year}-{cur.datetime.month}-{cur.datetime.day}'
    with open(f'logins_{w_datetime}.csv','a') as file:
        writer = csv.writer(file)
        writer.writerow(w_info)