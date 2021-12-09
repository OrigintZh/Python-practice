def Func(num):
    if num<=1:
        return 1
    return num * Func(num-1)
print(Func(10))
