import random

lower = "abcdefghijklmnoprstuvwxyz"
upper = "ABCDEFGHIJKLMNOPRSTUVWXYZ"
numbers = "123456789"

all = lower+upper+numbers

lenght = 16
password = "".join(random.sample(all,lenght))
print("Size özel yaratılan şifre: "+password)