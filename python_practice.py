
# from sympy import factorial
# print(factorial(5))

# n=5
# fact=1
# while n>=1:
#     fact=fact*n
#     n=n-1
# print(fact)

# Armstrong Number
# n=153
# s=str(n)
# l=len(s)
# k=0
# for i in range(l):
#     k=k+int(s[i])**l
# print(k)


# for i in range(1,101):
#     p=[]
#     for j in range(1,i+1):
#         if i%j==0:
#             p.append(i)
#     if len(p)==2:
#         print(i)

# n=1
# a=0
# b=1
# z=a+b
# while n<10:
#     a=b
#     b=z
#     z=a+b
#     n=n+1
#     print(z)




# l=["abc",11,2,6,33,7,3,53,2,6,"xyz"]
# lt=[11,2,6,33,7,3,53,2,6]
# l[0],l[-1]=l[-1],l[0]
# l.clear()
# s="devendra"
# print(s[::-1])
# l=l[::-1]
# print(l)

# n=0
# for i in lt: n=n+i
# print(n)

# print(reduce(lambda a,b:a+b,lt))

# lt.sort()
# print(lt[0],lt[-1])
# print(lt[-5:])

# m1=[i for i in lt if i%2==0]
# m2=[i for i in lt if i%2!=0]
# print(m1,m2)
    
# l=["abc",11,2,6,33,7,3,53,2,6,"xyz"]
# k=l.count(6)
# print(k)

# lt=[11,2,6,33,7,3,53,2,6]
# j=0
# for i in lt:
#     j=i+j
#     print(j)

# s=sorted(lt)
# print(s)
# lt.sort()
# print(lt)

# s="malayalam"
# if s==s[ : :-1]:
#     print("It is pelindrome")
# else: 
#     print("not pelindrome")
    
# s="malayalam"
# k=s.replace("m"," ",1)
# st=s[:2]+s[3:]


# s="Gfg is best . Geeks are good and Geeks like Gfg"
# st=s.count("is")
# print(st)

# if "is" in s:
#  print("Yes")

# if s.count("is")>0:
#     print("Yes")

# s="Gfg is best . Geeks are good and Geeks like Gfg"
# for k in s.split():
#     print(k,s.count(k),end=" ")

# d={k:s.count(k) for k in s.split()}
# print(d)

# st="devendra"
# l=[]
# vowel="aeiou"
# for char in st:
#     if char in vowel:
#         l.append(st)    
# print(set(l))

# st="devendra"
# l=list(st)    
# st=set(l)
# for i in st:
#     print(i,end="")

# s="GeeksForGeeks"
# x=s.isalnum()
# if x==True:
#     print(f"string {s} have Valid charectors.")
# else:
#     print(f"String {s} have spacial charrectors.") 

# s="Geeks For Geeks"
# st=s.split()
# k="-".join(st)
# print(k)

# s= 'geeksforgeeks'
# j=0
# for i in s:
#     k=s.count(i)
#     if k<2:
#         print(i,k)

# s= 'geeksforgeeks'
# a=[] 
# for i in s:
#     k=s.count(i)
#     if k>1:
#         a.append(i)
# print(set(a))

# s= 'geeks for geeks'
# d={k:s.count(k) for k in s.split()}
# print("geeks",d.get("geeks"))


# test_list = [1, 3, 5, 6, 3, 5, 6, 1]
# res = []
# [res.append(x) for x in test_list if x not in res]
# print(res)

# test_list = [1, 3, 5, 6, 3, 5, 6, 1] 
# res = []
# for i in test_list:
#     if i not in res:
#         res.append(i)
# print(res)

# n=5
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)

# n=153
# s=str(n)
# k=0
# for i in range(0,len(s)):
#    k=k+int(s[i])**len(s)
# if k==n:
#     print("It is armstrong number")
# else:
#     print("invalid armstrong")

# x=1
# y=1
# z=1
# for i in range(0,10):
#     x=y
#     y=z
#     z=x+y
#     print(z)
        
# n=7
# k=[]
# for i in range(1,n+1):
#     if n%i==0:
#         k.append(i)
# if len(k)==2:
#     print("It is prime")
# else:
#     print("Not prime")


# for i in range(1,101):
#     k=[]
#     for j in range(1,i+1):
#         if i%j==0:
#             k.append(j)
#     if len(k)==2:
#         print(i)        


# for i in range(1,5):
#     print(i*"*")
    
# n=20
# s=20
# j=0
# for i in range(1,s):
#     print(n*" ",i*"*"+j*"*")
#     n=n-1
#     j=j+1

# num=10
# for i in range(0,10):
#     print(n)
#     num=num-1

# for even in range(1,10):
#     if even%2==0:
#         print(even)

# j=0
# for i in range(0,4):
#     j=j+i**2
# print(j)

# d={"a":1,"b":3}
# x=d["a"]
# print(x)
# v=d.values()
# k=d.keys()
# print(v)
# print(k)
# g=d.get("a")
# print(g)

# l=[2,9,4,78,5]
# max=l[0]
# for i in range(1,len(l)):
#     if(l[i]>max):
#         max=l[i]
# print(max)

# """""""""""""""""""""""""Sorting""""""""""""""""""""
# l=[1,8,3,2,7,4]
# for i in range(0,len(l)):
#     for j in range(0,len(l)):
#         if l[i]<l[j]:
#             l[i],l[j]=l[j],l[i]      
#             print(l)


# import random
# import numpy as np
# r=np.random.randint((1,6),3)
# print(r)

# import random
# #Generate 5 random numbers between 10 and 30
# randomlist = random.sample(range(10, 30), 5)
# print(randomlist)

# """""""""""""""""""""""""Permutaion""""""""""""""""""""
# l=[3,2,1]
# for i in range(0,len(l)):
#     for j in range(0,len(l)):
            # l[i],l[j]=l[j],l[i] 
#             print(l)

# """""""Increase tuple""""       
# t1=(1,2,3)
# t2=(4,5,6) 
# t1=t1+t2
# print(t)

# s1="abc de f   "
# s2="bca"
# if sorted(s1)==sorted(s2):
#     print("It is anagram")

# print(list(s1))
# print(s1.split("-"))
# print(".".join(s1),end=" ")
# print(s1.replace(" ",""))


# import re
# s1="abc de f   "
# w=r"\s+"
# after=re.sub(w,"",s1)
# print(after)


# s1="abc de f   "
# s=[]
# for i in range(0, len(s1)):
#     if not s1[i]==" ":
#         # print(s1[i])
#         s.append(s1[i]) 
# print(''.join(s),end="") 


# s1="abc de ff   "
# d={k:s1.count(k) for k in s1.split() }
# print(d)

# test_list = [1, 3, 5, 6, 3, 5, 6, 1]
# res = []
# [res.append(x) for x in test_list if x not in res]
# print(res)

# l=[1,2,33,4,55,3,3,6,7,8,55,5,9,9,2]
# x=list(map(lambda a:a*a,l))
# print(x)
# y=list(filter(lambda a:a>10,l))
# print(y)
# z=reduce(lambda a,b:a+b,l)
# print(z)

# """"""""""remove duplicate"""
# l=[1,2,33,4,55,3,3,6,7,8,55,5,9,9,2]
# k=[]
# for i in l:
#     if i not in k:
#           k.append(i)
# print(k)

# l=[24,3,48,5,22,11]
# m=l[0]
# for i in range(0,len(l)):
#     if l[i]>m:
#        m=l[i] 
# print(m)

# print(list(i for i in range(0,11)))

# str="abcdefg"
# x=str[-3:-6:-1]
# print(x)

# import validators
# valid=validators.url('https://www.codespeedy.com/')
# if valid==True:
#     print("Url is valid")
# else:

#     print("Invalid url")

# Number = 123   
# Reverse = 0    
# while(Number > 0):    
#     Reminder = Number %10   
#     Reverse = (Reverse *10) + Reminder    
#     Number = Number //10    
# print("\n Reverse of entered number is = %d" %Reverse)
# print("Reverse of entered number is =",Reverse )

# n=123
# rev=0
# while n>0:
#     rem=n%10
#     # print(rem)
#     rev=(rev*10)+rem
#     print(rev)
#     n=n//10
#     # print(n)
# # print(rev)   

# def deco(abc):
#     def inner():
#         abc()
#         print("Devendra")
#     return inner
# @deco
# def abc():
#     print("Hello")
# abc()    

# def deco(add):
#     def inner():
#         a=add()
#         b=a+4
#         print(b)
#     return inner   
# @deco
# def add():
#     a=56
#     return a
# add()


# import json
# # some JSON:
# x =  '{ "name":"John", "age":30, "city":"New York"}'
# # parse x:
# y = json.loads(x)
# # the result is a Python dictionary:
# print(type(y),y["age"])
# print(y)

# import json
# # a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }
# # convert into JSON:
# y = json.dumps(x)
# # the result is a JSON string:
# print(type(y),y)


# print(ord("c"))
# print(chr(99))


# import sys
# t=(1,2,3,4)
# l=[1,2,3,4]
# print(sys.getsizeof(t), sys.getsizeof(l))


