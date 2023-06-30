# def outerfun(add):
#     def inner():
#         x=add()
#         y=x+5
#         print(y)
#     return inner
# @outerfun
# def add():
#     a=5
#     return a
# add()



# l=[1,2,3,4]
# input_length=2
# l1=[]
# if input_length==1:
#     for i in range(0,len(l)):
#         l1.append([l[i]])
# elif input_length==2:
#     for i in range(0,len(l)-1):
#         l1.append(l[i:i+2])
# else:
#     pass
# print(l1)


###count the vowel in string

# s='appleoraeonge'
# v='aeiou'
# l=[]
# for i in s:
#     if i in v:
#         l.append(i)
#         print(i)
# print(len(l))
         

########credit card numbr
# s="1234432156784444"
# x=list(s)
# for i in range(len(x)):
#     print(s[i])
#     if i<(len(x)-4):
#         x[i]="*"
# print(''.join(x))
        
        
####repeat the number

# s="now"
# k=""
# for i in s:
#     k=k+i*2
# print(k)


        
        
        
#!/bin/python3

# import math
# import os
# import random
# import re
# import sys



# if __name__ == '__main__':
#     n = int(input().strip())
#     if (n%2==0 & 2<n<5) | (n%2==0 and n>20):
#         print("Not Weird")
    
#     elif n%2==0 and 6<n<20:
#         print("Weird")
#     else:
#         print("Weird")  

# s='Dev'
# print(s.swapcase())


# num=123
# rev=0
# while num>0:
#     rem=num%10
#     rev=rev*10+rem
#     num=num//10
# print(rev)

####Sorting String#######
# st="devendra"
# ns=[]
# for i in list(st):
#     ns=[x for x in ns if x<i]+[i]+[x for x in ns if x>=i]
# print(''.join(ns))

l = [52,44,5,7,3,2,8,21]
def desc_ord_list():
    for i in range(len(l)):
        for j in range(i):
            if l[i]>l[j]:
                l[i],l[j]=l[j],l[i]
    print(l)          
# desc_ord_list()


def asc_ord_list():
    for i in range(len(l)):
        for j in range(i):
            if l[i]<l[j]:
                l[i],l[j]=l[j],l[i]
    print(l)
# asc_ord_list()


def max_number():
    max=l[0]
    for i in l:
        if max<i:
            max[0]=i
    print(max)
# max_number()


s="devendra"
def reverse_string():
    rev=""
    for i in range(len(s)):
        rev=s[i]+rev
    print(rev)
# reverse_string()


s="this is my pen"
k=s.split()
revl=[]
for i in k:
    rev=""
    for j in range(len(i)):
        rev=i[j]+rev
    revl.append(rev)
# print(*revl)


# s="devendra"
# l=[23,63,13,4,2,5,7975,6]
# len_list=len(l)
# k=[]
# for i in range(len_list):
#     k.append(l[len_list-i-1])
# print(k)


# s="devendra"
# print(s[::-1])
# print(''.join(list(reversed(s))))


s="devendra"
dup=[]
unique=[]
for i in s:
    if i not in unique:
         unique.append(i)
    else:
        dup.append(i)
print(dup)



