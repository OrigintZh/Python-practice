def min_common_divisor(a,b):
    if a<b:
        a,b = b,a
    c = a% b
    while(c):
        a = b
        b = c
        c = a%b
    return b

a = int(input("first number: "))
b = int(input("second number: "))
print(min_common_divisor(a,b))
