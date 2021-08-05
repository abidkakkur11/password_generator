#password generator
import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num ="1234567890"
special ="[]}{()*#@-_+$"

all=lower+upper+num+special
print("enter the length")
length =int(input())
password ="".join(random.sample(all,length))
print(password)
print("\n")
