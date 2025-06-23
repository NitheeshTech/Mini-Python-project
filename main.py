import random

print("Welcome to random password generator!")

randomechars = "ABCDEFGHIJKLMNOPQSTURYXZaqwszxderfcvgtyhbnjuikmlop@#₹&?+*"

nbrofpwds = int(input("Please enter the number of passwords to generate: "))
pwdlen = int(input("Please enter the length of each password: "))

print("Here are your random passwords:")

for x in range(nbrofpwds):
    pwd = ""
    for chars in range(pwdlen):
        pwd += random.choice(randomechars)
    print(pwd)
