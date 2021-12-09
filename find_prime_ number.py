def find_prime_number(num):
    for i in range(2,num+1):
        for j in range(2,int(i / 2)+1):
            if i % j == 0:
                break
        else: print(i)
        
find_prime_number(100)
