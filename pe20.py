'''
Exercise 20

Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

Extras:
Use binary search.
'''

import random
    
def normal_find(o_list, e_find):
    if e_find in o_list:
        print('yes')
    else:
        print('no')
        
def binary_find(o_list, e_find):
    s_index=0
    e_index=len(o_list)-1
    t=0
    while t==0 and s_index<=e_index:
        m_index=int((s_index+e_index)/2)
        if e_find<o_list[m_index]:
            e_index=m_index-1
        elif e_find>o_list[m_index]:
            s_index=m_index+1
        else:
            t=1
            print('The number is in the list ranking No.',m_index)
    if t==0:
        print('The number is not in the list.')
        print(m_index)
        if e_find>o_list[m_index]:
            print('1 It should rank at No.',m_index+2)
        else:
            print('2 It should rank at No.',m_index+1)
            
if __name__=='__main__':
    a=random.sample(range(501),10)
    temp=0
    for i in range(10):
        for j in range(i):
            if a[j]>a[i]:
                temp=a[j]
                a[j]=a[i]
                a[i]=temp
    print(a)
    b=random.randint(0,500)
    print(b)
    binary_find(a,b)      