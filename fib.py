def func(num):
    fib = [1,]
    for i in range(num):
        if i<2: fib.append(i+1)
        else: fib.append(sum(fib[-2:]))
    return fib
print(func(10))
