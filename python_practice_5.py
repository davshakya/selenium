# import re

# st = "Devnedr aeoi12. 3344#$%^&#5678"

# s=re.findall(r"\d+",st)
# s=re.findall(r"\D+",st)
# s=re.findall(r"\d+\.\d+",st)
# s=re.findall(r"\w+",st)
# s=re.findall(r"[a,e,i,o,u]",st)
# s = re.search("ae", st)
# print(s)


# l=["a","b","c"]
#
# x=iter(l)
# print(next(x))
# print(next(x))
# print(next(x))


# b = "HelloWorld!123"
# s=b[2:5]
# print(s)
# print(b.upper())
# print(b.lower())
# print(b.replace("H","K"))
# print(b.split(''))
# print(list(b))
# for i in b:
#     print(i, end="")
# print(b.count("o"))


# k=[]
# for i in b:
#     if i.isdigit():
#         print("This is Number",i)
#         k.append(i)
# print(k)


# b = "HelloWorld!123"
# d={i:b.count(i) for i in b}
# print(d)
# k=d.keys()
# v=d.values()
# print(k)
# print(v)
# print(d.items())

# for i, j in d.items():
#     if j>=2:
#         print(i, j)
# print(d["H"])

# dt={'e': 3, 'l': 1, 'o': 2}
# rd={values:keys for keys,values in dt.items()}
# print(rd)

# data_list = [5, 0, 23, 6, 23, 67]
# new_list_asc  = []
# new_list_desc  = []
# # Sort function
# for i in data_list:
#     new_list_asc = [ x for x in new_list_asc if x < i] + [i] + [ x for x in new_list_asc if x >= i ]
# print(new_list_asc)
#
# for i in data_list:
#     new_list_desc = [ x for x in new_list_desc if x > i ] + [i] + [ x for x in new_list_desc if x <= i ]
# print(new_list_desc)


# data_list = [5, 0, 23, 6, 23, 67]
# sl=[]
# for i in data_list:
#     sl=[x for x in sl if x<i] +[i]+ [x for x in sl if x>=i]
# print(sl)

# l1 = [5, 0, 23]
# l2= [6, 23, 67]
# suml=l1+l2
# print(suml)



# s="devendra"
# ss=[]
# for i in list(s):
#     ss=[x for x in ss if x<i]+[i]+[x for x in ss if x>=i]
# print("".join(ss))


# st="devendra"
# rs=""
# for i in range(len(st)):
#     rs=st[i]+rs
# print(rs)



# data_list = [5, 0, 23, -6, 23, 67]
# max=[0]
#
# for i in range(len(data_list)):
#     if max[0]<data_list[i]:
#         max[0]=data_list[i]
# print(max)

#
# def outer(add):
#     def inner():
#         b=add()**2
#         print(b)
#     return inner()
#
# @outer
# def add():
#     a=5
#     return a
#
#
# import copy
# #
# old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
# new_list = copy.copy(old_list)
#
# old_list[1][1] = 'AA'
# print("Old list:", old_list)
# print("New list:", new_list)
# #
# #
# old_list1 = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
# new_list1 = copy.deepcopy(old_list1)
#
# old_list1[1][0] = 'BB'
# print("Old list1:", old_list1)
# print("New list1:", new_list1)


# number = 123321
# s = str(number)
# rs = ""
# for i in range(len(list(s))):
#     rs = s[i]+rs
# if s == rs:
#     print("It is polynomial")
# else:
#     print("it is not polynomial")




# num=123
# rev=0
# while num>0:
#     rem=num%10
#     rev=rev*10+rem
#     num=num//10
# print(rev)

# n=12345
# while n>0:
#     n=n//10
#     print(n)

#
# for i in range(1,5):
#     for j in range(i-1,i):
#         print(str(i)*i)

# row=3
# col=5
# for i in range(row):
#     for j in range(i):
#         print("*"*col)

#
# def creating_gen(index):
#     months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
#     yield months[index]
#     yield months[index+2]
# print(next(creating_gen(2)))


# s="deve"
# print(dir(s))


# import time
# s_time=time.time()
# s="cab413"
# ls=list(s)
# l=[]
# for i in ls:
#     l=[x for x in l if x<i]+[i]+[x for x in l if x>=i]
# e_time=time.time()
# print("".join(l))
# print(e_time-s_time)


# s_time=time.time()
# s="cab413"
# ls=list(s)
# for i in range(len(ls)):
#     for j in range(i):
#         if ls[i]<ls[j]:
#             ls[i], ls[j] = ls[j], ls[i]
# e_time=time.time()
# print(ls)
# print(e_time-s_time)

# l=[12,3,4,2,31]
# # print(sorted(l))
# l.sort()
# l.reverse()
# print(l)

# s="deves ha"
# k=s.split()
# print(k)

# s="man can san man can tan man tan"
# d={x:s.count(x) for x in s.split()}
# for keys, values in d.items():
#     if values>=2:
#         print(keys,values)
# # print(d)


# s="a3b2c4"
# ls=list(s)
# ns=""
# for i in ls:
#     if i.isalpha():
#         var=i
#     else:
#         ns=ns+var*int(i)
# print(ns)

# import sys
# print(sys.getsizeof("d"))

# print(ord('a'))
# print(ord("1"))
# print(chr(100))
# print(id('abc'))
# print(id('abc'))

# l=[12,2,34,4]
# l.reverse()
# print(l)

# import openpyxl
# wb=openpyxl.load_workbook("sample.xlsx")
# sht=wb["Sheet1"]
# cl=sht.cell(1,3).value
# for i in range(2,5):
#     print(sht.cell(i,3).value)

# import xlrd
# wb=xlrd.open_workbook("sample.xlsx")
# sheet=wb.sheet_by_index(0)
# cell=sheet.cell_value(2,2)
# print(cell)



# f=open("test.txt", "r+")
# f.write("Hello shakya manan")
# # p=f.read()
# p=f.readlines()
# print(p)
# f.close()




###Reverse line of text###########
# s="This my pen which is not your"
# sl=s.split()
# l=[]
# for i in sl:
#     k=""
#     for j in range(len(list(i))):
#         k=i[j]+k
#     l.append(k) 
# print(" ".join(l)) 



# print('hi \
#       frined')

# print('hi \nfrined')

# print(''' Hello
#       firend''')

# print('a\bgt')
# print('a\\abc\g')
# print('a\n\g')
# print('atg\rg')
# print('a\tb\g')
# print('a\a\g')
# print(ord("N"))
# print(ord("1"))
# print(hex(15))
# print(oct(15))
# print(bin(5))
# print("Ram \u20b9 500")
# print(ord("₹"))
# print("Ram \u20B9 500")


#######Refrence values #####

# a=2,3
# print(type(a))
# a,b=3,4
# print(a)
# a=b=c=d=3
# print(a)

# a,*b,c=1,2,3,4,5,6,7,8,9,10,11,12,13
# print(b)

# a=[1,2,3]
# c=a.copy()
# c.append(4)
# print(id(c),c)
# print(id(a),a)
# b=a
# b.append(7)
# print(id(b),b)

# print("xyz".upper())



# print(type(3))
# print(isinstance(3,int))
# print(isinstance('a',str))

####Dynamic type python ####
# a=2
# print(type(a))
# a="Hello"
# print(type(a))

######some_other_dataype##########
# print(frozenset({1,2,3,4,4}))
# print(type(range(0,5)))
# print(b'Hello')
# print(bytearray(5))
# x=memoryview(bytes(5))
# print(x)

#####Type casting ####
# print(complex(5))
# print(int(5.3))
# print(float(5))
# print(type(str(123)))
# print(bool(""))
# print(bool("hello"))
# print(bool(-12.1))
# print(bool(0))

###### f strings ####
# a="Devendra"
# z=f"Hello my name is {a}."
# print(z)


#### bytes to string ####
# bt=(b'I LOVE INDIA')
# print(bt)
# st=str(bt, 'UTF8')
# print(st)

# print(40//10)
# print(5%2)

####Python Operator########
import math
# print(5-+-2)
# a=44
# b=5
# c=a/b
# i=a//b
# print(c)
# print(i)

# x=2.6
# print(math.floor(x))
# print(math.ceil(x))

# x=2.6
# print(round(x))
# z=2.2
# print(round(z))
# d=2.5
# print(round(d))
# print(2**3)
# print("*"*3)
# print(0/1)
# print(3.4%3.2)
# a="A"
# b="a"
# print(a==b)
# print(a>b)
# print(a<b)
# print(True>False)
# print(bool(""))
# print(not(""))


# Logical
# j="" or ""
# c= "" or "Hi"
# a= "Hello" or ""
# k="Hello" or "hi"
# print(a)
# l="" and ""
# d= "hello" and "Hi"
# s="Hello" and ""
# e= "" and "Hi"

#bitwise
# print(s)
# print(~9)
# print(~-9)
# print(1 & 0)
# print(0 | 1)
# print(3 & 8)
# print(3 | 8)
# print("hi" & "hello")
# print("hi" | "hello")
# print(3 ^ 7)
# print(4<<2)
# print(5>>2)
# print(True & False)
# print(True | False)


########## Function ############
# import sys
# print("x",sep='',end='\n',file=sys.stdout,flush=True)
# print("a","b", sep="*",end='$')
# print("a",file=sys.stdout)
# print("a"     "b",sep="---")
# print("a", "b",sep="---")
# print("Hi"+"Hello")
# print("Hi","Hello")
# a=4
# print("a=",a)
# print(["Hi","Hello", 4],sep="*")
# print(*["Hi","Hello", 4],sep="*")
# print(*["Hi","Hello", 4])
# print(["Hi","Hello", 4])

file1=open("file1.txt","w")
print("Hello This is Dev", file=file1)
file1.close()










