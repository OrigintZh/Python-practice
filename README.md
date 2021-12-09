# Python-practice
# python期末复习的一些算法

#求阶乘
```python
def Func(num):
    if num<=1:
        return 1
    return num * Func(num-1)
print(Func(10))
```

#辗转相除法求最小公倍数
```python
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
```

#找一百以内的素数
```python
def find_prime_number(num):
    for i in range(2,num+1):
        for j in range(2,int(i / 2)+1):
            if i % j == 0:
                break
        else: print(i)
        
find_prime_number(100)
```

```求斐波那契数
def func(num):
    fib = [1,]
    for i in range(num):
        if i<2: fib.append(i+1)
        else: fib.append(sum(fib[-2:]))
    return fib
print(func(10))
```
