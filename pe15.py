'''
Exercise 15

Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

  My name is Michele
Then I would see the string:

  Michele is name My
shown back to me.
'''

def reverse_word(a):
    start=0
    word_list=[]
    for n in range(0,len(a)):
        if a[n]==' ':
            word_list.append(str(a[start:n]))
            start=n+1
    if a[len(a)-1]!=' ':
        word_list.append(str(a[start:len(a)]))
    word_list.reverse()
    return word_list

def split_word(a):
    x=a.split()
    x.reverse()
    return x
    
a=input('Please enter a sentence: ')
#b=reverse_word(a)
b=split_word(a)
'''
print(b)
for n in range(0,len(b)-1):
    print(b[n], end=' ')
print(b[len(b)-1])
'''
print(" ".join(b))
