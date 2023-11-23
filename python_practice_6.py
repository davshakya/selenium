# l=[2,5,12,4,7,78]
# newlist=[]
# for i in l:
#     newlist=[x for x in newlist if x<i]+[i]+[x for x in newlist if x>i] 
# print(newlist)

# newlist=[l[0]]
# for i in range(len(l)):
#     if newlist[0]>l[i]:
#         newlist[0]=l[i]
# print(newlist)    

# s='devendra'
# rev=''
# for i in s:
#     rev=i+rev
# print(rev)

# st="This my pen"
# k=[]
# for i in st.split():
#     rev=''
#     for i in i:
#         rev=i+rev
#     k.append(rev)    
# print(' '.join(k))

# for i in range(1,6):
#     print("*"*i+" "*(5-i)*2+"*"*(i))

# for i in range(1,6):
#     print(" "*(5-i)+"*"*(i))

# for i in range(1,6):
#     print("*"*(6-i))
 


# l=[2,5,12,4,7,78]

# for i in range(len(l)):
#     for j in range(i):
#         if l[i]>l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l)

       
# max=[l[0]]        
# for i in range(len(l)):
#     if max[0]<l[i]:
#         max[0]=l[i] 
# print(max[0])  


# import time
# start1=time.time()
# n=13123456
# l=[]
# i=1
# while(i<=n):
#     if n%i==0:
#         l.append(i)
#     i=i+1
# if len(l)==2:
#     print("It is prime number")
# else:
#     print("Not a prime number")
# print("With list==",time.time()-start1)     


# start2=time.time()
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
    
# print("without list",time.time()-start2)     
        


# num=123
# rev=0
# while num>0:
#     rem = num%10
#     rev=rev*10+rem
#     num=num//10
# print(rev)


# n=10
# x=0
# y=1
# for i in range(n):
#     z=x+y
#     x=y
#     y=z
#     print(z)

# l=[24,35,1,114,22,5]
# for i in range(len(l)):
#     for j in range(i):
#         if l[i]<l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l)  

# l=[24,35,1,114,22,5]
# max=[l[0]]
# for i in range(len(l)):
#     if l[i]<max[0]:
#         max[0]=l[i]
# print(max[0])

# d={"z":5}

# l=["a","b","c"]
# l2=[1,2,3]
# for i in range(len(l)):
#     d[l[i]]=l2[i]
# print(d)

# d3={"x":4,"y":8}
# # d.update(d3)
# print(d3.get("x"))
# # print(3)


# x=5
# print(isinstance(x,int))
    
# s="Devnedra"
# d=s.lower()
# dd=""
# for i in d:
#     if i not in dd:
#         dd=dd+i 
# print(dd)

# c=1
# k=5
# for i in range(5):
#     for j in range(1,k-i):
#         print(c,end=" ")
#         c=c+1
#     print("\n")    

# import re
# s="devendr12347890#$%^"
# x=re.findall("\W",s)
# print(x)




# s="devendra"
# k=""
# for i in s:
#     k=i+k
# print(k)

# num=123
# rev=0
# while num>0:
#     rem=num%10
#     rev=rem*10+rev
#     num=num//10
# print(rev)


# s="devendra singh shakya"
# rev=""
# for j in s.split():
#     k=""
#     for i in j:
#         k=i+k
#     rev=rev+ " " + k  
# print(rev)

# k=5
# m=1
# for i in range(6):
#     print(k*f"{m}"+i*' ')
#     k=k-1
#     m=m+1
    
    
k=6
m=1
for i in range(1,5):
    for j in range(1,k-i):
        print(m,end=" ")
        m=m+1
    print("\n")