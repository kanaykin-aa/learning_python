def two_sum(numbers, target):
    x=[]
    for i, k in enumerate(numbers):
        for l, m in enumerate(numbers):
            if k+m==target and i!=l:
                x.append(i)
                x.append(l)
                return tuple(x)