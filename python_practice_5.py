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




