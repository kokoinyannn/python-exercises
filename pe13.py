'''
Exercise 13

Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
'''

def Fib(a):
    fib1=1
    fib2=1
    print(fib1);print(fib2)
    for n in range(0,a):
        temp=fib2
        fib2=fib1+fib2
        fib1=temp
        print(fib2)

a=int(input('How many Fibonnaci numbers do you want? '))
Fib(a)