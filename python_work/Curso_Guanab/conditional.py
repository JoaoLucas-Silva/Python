'''
name = str(input("What is your name? ")).strip()

if len(name) - name.count(" ") >= 10:
    print("\nYour name is big !!")
else:
    print("\nYour name is small !!")
'''

from random import randint

num_c = randint(0,5)

num = int(input("What number am i thinking of? "))

if num == num_c:
    print("\Congratulations, you win!!!")
else:
    print("\nYou lost!!!")
    