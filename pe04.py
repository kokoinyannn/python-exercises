'''
Exercise 4

Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
'''

num=int(input('Enter a number: '))
divisors=[]
for i in range(1,num+1):
    if num%i==0:
        divisors.append(i)
print(divisors)

#challenge: 减少比较次数
divisors_2=[]
max=num
for i in range(1,max):
    if num%i==0 and int(num/i)>=i:
        divisors_2.append(i)
        if int(num/i)!=i:
            divisors_2.append(int(num/i))
        max=int(num/i)+1
result=sorted(divisors_2)
print(result)