'''
Exercise 6

Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
'''

s=input('please enter a string: ')
l=len(s)
p=1
if l%2==0:
    for n in range(0, int(l/2)):
        if s[n]!=s[l-1-n]:
            p=0
            print('This string is not a palindrome.')
            break
    if p==1:
        print('This string is a palindrome.')            
else:
    for n in range(0, int((l-1)/2)):
        if s[n]!=s[l-1-n]:
            p=0
            print('This string is not a palindrome.')
            break
    if p==1:
        print('This string is a palindrome.')
        
#其实不用区分长度的奇偶，因为偶数时(l/2-1)和奇数时((l-1)/2-1)取整后相同。

#利用截取列表的方法
#去掉空格，可用race car测试
s=input('please enter a string: ')
s=s.replace(' ','')
rs=s[::-1] #list[start_index:end_index:step]
if s==rs:
    print('This string is a palindrome.')
else:
    print('This string is not a palindrome.')