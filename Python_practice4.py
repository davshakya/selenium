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