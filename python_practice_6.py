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
        




