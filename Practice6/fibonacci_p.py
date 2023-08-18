def fib(n):
    old, new = 0, 1
    for i in range(n):
        old, new = new, old + new
        print(old)
print(fib(6))