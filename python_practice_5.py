import locale
import re

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
s="This my pen which is not your"
sl=s.split()
l=[]
for i in sl:
    k=""
    for j in range(len(list(i))):
        k=i[j]+k
    l.append(k) 
print(" ".join(l)) 

