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



l=[1,2,3,4]
input_length=2
l1=[]
if input_length==1:
    for i in range(0,len(l)):
        l1.append([l[i]])
elif input_length==2:
    for i in range(0,len(l)-1):
        l1.append(l[i:i+2])
else:
    pass
print(l1)