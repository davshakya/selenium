#
# import re
# s="Gfg is best &*&*. Geeks are good 123 and Geeks like Gfg"
#
# r=re.findall(r'\d{3}',s)
# print(r)


# class Person:
#     def __init__(self, age, name):
#         self.age = age
#         self.name = name
#
#     def __hash__(self):
#         print('The hash is:')
#         return hash((self.age, self.name))
#
#
# person = Person(23, 'Adam')
# print(hash(person))

#
# r=re.findall(r'\d{3}',s)
# # r=re.findall(r'[a-zA-Z]',s)
# r=re.findall(r'[^\w\s]',s)
#
# print(r)

# s1="abc de f   "
# s=[]
# for i in range(0, len(s1)):
#     if not s1[i]==" ":
#         # print(s1[i])
#         s.append(s1[i])
# print(''.join(s),end="")


# st=""
# for i in s.split():
#     st=i+" "+st
# print(st)


# for i in s:
#     if s.count(i)>2 and i!=" ":
#         print(i,s.count(i))


# for k in s.split():
#     print(k,s.count(k),end=" ")

# d={k:s.count(k) for k in s}
# print(d)

import random
st="devendra"
print(random.sample(st,2))
print(random.randrange(1,20,3) )
print(random.SystemRandom.randint(1,12))

