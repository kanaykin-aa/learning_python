def persistence(n):
    z=0
    while n>9:
        x=1
        for i in str(n):
            x*=int(i)
        n=x
        z+=1
    return z