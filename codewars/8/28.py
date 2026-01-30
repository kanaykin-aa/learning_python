def count_sheep(n):
    if n==0:
        return ""
    x=[]
    for i in range(1,n+1):
        x.append(str(i)+' '+'sheep...')
    return ''.join(x)