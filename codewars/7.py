def reverse_seq(n):
    x=[]
    for i in range(n+1):
        x.append(i)
    x.reverse()
    x.pop()
    return x