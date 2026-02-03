def dig_pow(n, p):
    n=str(n)
    x=[]
    y=[]
    for i in n:
        x.append(i)
    for l, m in enumerate(x, p):
        y.append(int(m)**l)
    if sum(y)%int(n)==0:
        return sum(y)//int(n)
    else:
        return -1