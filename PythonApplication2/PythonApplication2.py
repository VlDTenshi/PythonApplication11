from mymodule1 import *


list_name = []
list_password = []
print("Hello new/old user")

print("Choose your way:")

i=0

while True:
    a=input(str("Sign in/Create account/Finish work:?"))
    if i == 1:
        break
    i+=1
l=get_login("Vladimir Dudakov")
print("l")
