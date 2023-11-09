import time

# def deco(add):
#     def inner():
#         b=add()+4
#         print(b)
#     return inner

# def add():
#     a=56
#     return a
# b=deco(add)
# b()

##############################

# def deco(add):
#     def inner():
#         b=add()+4
#         print(b)
#     return inner

# @deco
# def add():
#     a=56
#     return a
# add()


# def timer(func):
#     def wrapper():
#         start=time.time()
#         func()
#         print("time taken by",func.__name__,time.time()-start, "sec")
#     return wrapper

# @timer
# def hello():
#     time.sleep(2)
#     print("hello")
# hello()
        
# @timer
# def display():
#     time.sleep(3)
#     print("dipslay")
# display()
        
# ###########################

# def timer(func):
#     def wrapper(*args):
#         start=time.time()
#         func(*args)
#         print("time taken by",func.__name__,time.time()-start, "sec")
#     return wrapper

# @timer
# def display():
#     time.sleep(3)
#     print("dipslay")
# display()

# @timer
# def square(n):
#     time.sleep(1)
#     print(n**2)
# square(4)


######################################
  
# def checkdatatype(datatype):
#     def wrpapper1(func):
#         def wrapper2(*args):
#             if type(args[0])==datatype:
#                 func(*args)
#             else:
#                 raise   TypeError("ye datatype sahi nai hai")
#         return wrapper2
#     return  wrpapper1
    
# @checkdatatype(int)
# def sanitycheck(n):
#     print(n**2)
# sanitycheck(3)


###################################

# def deco_test(limit):
#     def outer(normal_fun):
#         def inner(*args):
#             if args[0]>=limit:
#                 normal_fun(*args)
#             else:
#                 print("Enter value greater than",limit)
#         return inner
#     return  outer

# @deco_test(7)
# def normal_fun(n):
#     print(n**2)
# normal_fun(9)        

    
#######################

def deco(func):
    def inner():
        x=func()
        x=x+5
        print(x)
    return inner

@deco
def func():
    return 8
func()
    
    

   