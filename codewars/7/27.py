def factorial(n):
    if n < 0 or n > 12:
        raise ValueError("значение меньше 0 или больше 12")
    elif n==0:
        return 1
    x=1
    for i in range(1,n+1):
        x*=i
    return x