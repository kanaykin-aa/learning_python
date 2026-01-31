def divisors(n):
    x=[]
    for i in range(1,500000):
        if n%i==0:
            x.append(i)
    return len(x)