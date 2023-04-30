# import random
# a = 5
# b = 10
# max_iterations = random.randint(0,10)
# count = 0
# while count < a or count < b and not count >= max_iterations:
#     print(f"count: {count}, a: {a}, b: {b}")
#     count += 1


s="wewewrtret"
st=''

for i in s:
    if i not in st:
        st=st+i
    elif i in st:
        st=st+"$"
    else:
        pass
print(st)
