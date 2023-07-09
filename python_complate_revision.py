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
import copy
#
# old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
# new_list = copy.copy(old_list)

# old_list[1][1] = 'AA'
# print("Old list:", old_list)
# print("New list:", new_list)
# #
# #
# old_list1 = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
# new_list1 = copy.deepcopy(old_list1)

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
#     # yield months[index+2]
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

#### File handling with print function #######
# file1=open("file1.txt","w")
# print("Hello This is Dev", file=file1)
# file1.close()

##### Mysql ######

# import mysql.connector as connector
# mydb = connector.connect(host = "localhost", port=3306, user = "root", password = "tiger")  
# if mydb.is_connected():                                  
#     print("Connection Done")
# else:
#     print("Not Connected")
# mycursor = mydb.cursor()
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#   print(x)
# print(complex(3,5))
# print(bool(2+3j))

######## Number Conversion ######
# a=2
# b=31
# c=324.230
# print(f"a=%d b=%d" %(a,b))
# print(f"a=%d"% a)
# print(f"a=%d" %a)
# print(f"a=%#x" %b)
# print(f"a=%#o" %b)
# print(f"a=%f" %c)
# print(f"a=%g" %c)
# print(f"a=%e" %c)

##### Charector Conversion ##########
# i='A'
# print(f"i=%c"%i)
# print(f"%c"%'\101')
# print(f"%c"%'\x41')
# print(f"%c"%'\u20b9')
# print(f"%c"%'\U000020b9')

###### String conversion #######
# print(f"%s"%'Hello')
# print(f"%r"%'Hello')
# print(f"%a"%'Hello')

###### Insertion of  Charector#######
# print(f"%d%%"%12)

#### Formating width specifier ######
# %[flags][witdh][.precision]type
# print(f"%f"%234)
# print(26)
# print(f"%-7d"%26)
# print(f"%-7d"%2632)
# print(f"%7d"%23316)
# print(f"%7d"%232996)
# print(f"%7s"%'*******')
# print(f"%7s"%'*****')
# print(f"%7c"%'*')

#### Precision specifier ########
# print(f"%.2f"%123.464456437)
# print(f"%4.3f"%123.4676547)
# print(f"%10.1f"%123.46


####### Padding with Zero usinf flag(#,0,+,-,'') ######
# print(f"%05d"%34)
# print(f"%05d"%346)
# print(f"%05d"%3481)

# print(f"%-05d"%34)
# print(f"%-05d"%346)
# print(f"%-05d"%3481)

# print(f"%+5g"%34)
# print(f"%+5g"%346)
# print(f"%+5g"%-3481)
# print(f"%-5g"%-3481)
# print(f"% g"%3481)
# print(f"%g"%3481)

###### F string in python #####
# a=3
# b=1
# print(f"sum of {a} and {b} is equal to {a+b}")
# a="Dev"
# b="shakya"
# print(f" Hello {a!r} and {b!r}")
# print('hello {}'.format("dev"))
# print("{0[name]:10} and {0[age]:10}".format({"name":"Dev", "age":36}))    
# print("{0[name]:>10} and {0[age]:<10}".format({"name":"Dev", "age":36})) 

######Ternary Operator #########
# a=10
# b=9
# c=12
# print(a if a>b else b)
# print((a,b)[a>b])
# print(("dev","shakya")[a>b])
# print(("dev","shakya")[a<b])
# print({True:"Yes",False:"No"}[a>b])
# print((lambda a:a, lambda b:b)[a>b])
# print("hello" if a>b else "hi" if a>c else "no")


####### odd even #######
# n=14
# print("even" if n%2==0 else "odd" )

##### Area of circle ######
# import math
# r=float(input("Enter the value of radius: "))
# area_of_circle=math.pi*r**2
# print("Area of circle is ",area_of_circle if r>0 else "Not allowed, Radius should be greater than 0")
 
##########area of square ######
# side=float(input("Enter the value of side:"))
# if side>0:
#     area=side*side
#     print(f'Area of square is %.2f'% area)
# else:
#     print("Cannot find area")


###### find the age #####
# age=int(input("Enter the age of person:"))
# if age>0 and age<100:
#     print(f"Age of the persion is %d"%age)
#     print(f"Age of the persion is {age}")
# else :
#     print("invalid age")
 

####### problem 1####
# n1=int(input())
# n2=int(input())
# n3=int(input())
# if n1!=n2 and n2!=n3 and n3!=n1:
#     print("1")
# else:
#     print("0")

####### problem 2####
# m,n =input().split()
# m=int(m)
# n=int(n)
# if m%n==0:
#     print(f'%d'%(m/n))
# else:
#     print("0")


######## Loops ########


"""It is indefinite loop"""
# n=int(input("Enter any number:"))
# i=1
# while i<=n:
#     print("Hello")
#     i=i+1
    
######## Prime Number#######

# n=int(input("Enter any number:"))
# flag=0
# i=2
# while(i<n):
#     if n%i==0:
#         flag=1
#         break
#     i=i+1
# if flag==1:
#     print("Not a prime number")
# elif n==1:
#     print("Not a prime number")
# else:    
#     print("It is prime number")        
        
        
#### for loop #####
# for a,b,c in [(1,2,3),(4,5,6), (7,8,9)]:
#     print(a,b,c)

# for a,*b,c in [(1,2,4,3),(4,5,5,6), (7,8,10,9)]:
#     print(a,b,c)

# for a in [(1,2,3),(4,5,6), (7,8,9)]:
#     print(a)


##### Iterable vs Iterator #########

# s="Hello"
# i=iter(s)
# # print(type(i))
# # k=list(i)
# # print(str(i))
# # t=tuple(i)
# # print(k)
# # print(t)

# # print(next(i))
# l=[1,2,3,3]
# k=iter(l)
# # print(next(k))
# # print(next(k))
# for i in k:
#     print(i)