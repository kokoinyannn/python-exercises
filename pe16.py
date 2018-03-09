'''
Exercise 16

Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

Extra:

Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
'''

import random

l=int(input('Length of the Password: '))
while l not in range(6,21):
    l=input('Length of the Password: ')

ul='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ll='abcdefghijklmnopqrstuvwxyz'
number=[]
for i in range(10):
    number.append(str(i))
sign='~!@#$%ˆ&*()-_=+,./;:{}[]<>\|'

len_ul=random.randint(1,l-3)
len_ll=random.randint(1,l-2-len_ul)
len_n=random.randint(1,l-1-len_ul-len_ll)
len_s=random.randint(1,l-len_ul-len_ll-len_n)

psw_ul=random.sample(ul,len_ul)
psw_ll=random.sample(ll,len_ll)
psw_n=random.sample(number,len_n)
psw_s=random.sample(sign,len_s)

psw=psw_ul+psw_ll+psw_n+psw_s
print(psw)
random.shuffle(psw)
print("".join(psw))